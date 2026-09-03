"""Pre-train benchmark ML models on the sample synthetic dataset."""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.app.models.schemas import ModelTrainRequest, ModelType
from backend.app.services.storage_service import storage_service
from backend.app.services.ml_service import ml_service


def main():
    print("Pre-training benchmark machine learning models on demo dataset...")
    df = storage_service.load_dataset("sample_synthetic_transactions.csv")
    req = ModelTrainRequest(
        dataset_name="sample_synthetic_transactions.csv",
        models_to_train=[
            ModelType.LOGISTIC_REGRESSION,
            ModelType.DECISION_TREE,
            ModelType.RANDOM_FOREST,
            ModelType.GRADIENT_BOOSTING,
            ModelType.ISOLATION_FOREST
        ],
        handle_imbalance=True,
        test_size=0.2,
        random_state=42
    )
    result = ml_service.train_models(df, req)
    print(f"Training complete! Best performing model: {result.best_model_name}")
    for m in result.models:
        print(f" - {m.model_name}: F1={m.f1_score:.4f}, Recall={m.recall:.4f}, Prec={m.precision:.4f}, Acc={m.accuracy:.4f}")


if __name__ == "__main__":
    main()
