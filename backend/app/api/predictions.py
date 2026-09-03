"""Prediction endpoints handling real-time single and batch transaction scoring."""

from typing import Dict, Any, List
from fastapi import APIRouter, HTTPException
import pandas as pd

from backend.app.models.schemas import SingleTransactionInput, PredictionResult, BatchPredictionRequest, SuspiciousItem, ReviewStatus
from backend.app.services.ml_service import ml_service
from backend.app.services.risk_service import risk_service
from backend.app.services.suspicious_service import suspicious_service
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/predictions", tags=["Predictions"])


@router.post("/single", response_model=PredictionResult)
def predict_single(req: SingleTransactionInput, model_name: str = None):
    """Run real-time fraud prediction and risk scoring for an individual transaction."""
    tx_dict = req.model_dump()
    is_suspicious, prob, used_model = ml_service.predict_single(tx_dict, model_name)

    result = risk_service.calculate_risk(tx_dict, prob, used_model)

    # If High Risk, route to suspicious queue for analyst review
    if result.risk_level == "HIGH":
        suspicious_item = SuspiciousItem(
            transaction_id=result.transaction_id,
            customer_id=result.customer_id,
            amount=result.amount,
            timestamp=tx_dict.get("timestamp", ""),
            location=tx_dict.get("location", "Unknown"),
            device_type=tx_dict.get("device_type", "Unknown"),
            risk_score=result.risk_score,
            risk_level=result.risk_level,
            review_status=ReviewStatus.NEW,
            flags=[f.factor for f in result.contributing_factors]
        )
        suspicious_service.add_or_update_suspicious_item(suspicious_item)

    history_service.record_action(
        action=f"Scored transaction {result.transaction_id}",
        category="PREDICTION",
        details={
            "amount": result.amount,
            "risk_score": result.risk_score,
            "level": result.risk_level,
            "model": result.model_used
        }
    )

    return result


@router.post("/batch")
def predict_batch(req: BatchPredictionRequest):
    """Execute batch fraud scoring on an entire dataset."""
    try:
        df = storage_service.load_dataset(req.filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{req.filename}' not found.")

    records = df.to_dict(orient="records")
    predictions: List[Dict[str, Any]] = []
    high_risk_count = 0
    med_risk_count = 0
    low_risk_count = 0

    for tx in records:
        is_suspicious, prob, used_model = ml_service.predict_single(tx, req.model_name)
        res = risk_service.calculate_risk(tx, prob, used_model)

        if res.risk_level == "HIGH":
            high_risk_count += 1
            suspicious_item = SuspiciousItem(
                transaction_id=res.transaction_id,
                customer_id=res.customer_id,
                amount=res.amount,
                timestamp=str(tx.get("timestamp", "")),
                location=str(tx.get("location", "Unknown")),
                device_type=str(tx.get("device_type", "Unknown")),
                risk_score=res.risk_score,
                risk_level=res.risk_level,
                review_status=ReviewStatus.NEW,
                flags=[f.factor for f in res.contributing_factors]
            )
            suspicious_service.add_or_update_suspicious_item(suspicious_item)
        elif res.risk_level == "MEDIUM":
            med_risk_count += 1
        else:
            low_risk_count += 1

        tx_pred = dict(tx)
        tx_pred["risk_score"] = res.risk_score
        tx_pred["risk_level"] = res.risk_level
        tx_pred["prediction_label"] = res.prediction_label
        predictions.append(tx_pred)

    # Save scored dataset
    scored_filename = f"scored_{req.filename}"
    storage_service.save_dataset(scored_filename, pd.DataFrame(predictions))

    history_service.record_action(
        action=f"Batch scored {len(records)} records in '{req.filename}'",
        category="PREDICTION",
        details={
            "total": len(records),
            "high_risk": high_risk_count,
            "medium_risk": med_risk_count,
            "low_risk": low_risk_count
        }
    )

    return {
        "message": f"Successfully processed {len(records)} transactions",
        "scored_dataset": scored_filename,
        "total_processed": len(records),
        "low_risk_count": low_risk_count,
        "medium_risk_count": med_risk_count,
        "high_risk_count": high_risk_count,
        "sample_preview": predictions[:5]
    }
