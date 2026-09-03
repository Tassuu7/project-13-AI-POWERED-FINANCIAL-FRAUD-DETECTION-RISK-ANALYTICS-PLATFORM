"""Tests for ML training, evaluation, and single inference."""

import pytest
import pandas as pd
from backend.app.models.schemas import ModelTrainRequest, ModelType
from backend.app.services.ml_service import ml_service
from backend.app.services.synthetic_generator import synthetic_generator
from backend.app.models.schemas import SyntheticGenerateRequest


def test_ml_service_train_and_predict():
    # Generate small dataset
    synth_req = SyntheticGenerateRequest(num_records=120, fraud_percentage=10.0, random_seed=7)
    df = synthetic_generator.generate(synth_req)

    train_req = ModelTrainRequest(
        dataset_name="in_memory_test.csv",
        models_to_train=[ModelType.LOGISTIC_REGRESSION, ModelType.RANDOM_FOREST],
        handle_imbalance=True,
        test_size=0.25
    )
    result = ml_service.train_models(df, train_req)

    assert len(result.models) == 2
    for m in result.models:
        assert m.accuracy > 0.8
        assert m.f1_score >= 0.0
        assert len(m.confusion_matrix) == 2

    # Single inference test
    sample_tx = {
        "amount": 200000.0,
        "previous_transaction_amount": 800.0,
        "distance_from_usual_location": 350.0,
        "transaction_frequency": 6,
        "device_type": "Unknown Device",
        "timestamp": "2025-01-01 02:30:00",
        "account_age_days": 15
    }
    is_suspicious, prob, model_name = ml_service.predict_single(sample_tx)
    assert is_suspicious == 1
    assert prob > 0.5
