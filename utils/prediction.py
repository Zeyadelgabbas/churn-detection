from .validation import CustomerData
from .config import PREPROCESSOR_FILE_PATH , XGB_MODEL_PATH , FORREST_MODEL_PATH
import joblib
import pandas as pd



def predict_new(data:CustomerData):

    preprocessor = joblib.load(PREPROCESSOR_FILE_PATH)
    xgb_clf = joblib.load(XGB_MODEL_PATH)
    forest_clf = joblib.load(FORREST_MODEL_PATH)

    data = pd.DataFrame([data.model_dump()])
    X_preprocessed = preprocessor.transform(data)

    predictions = {
        "xgb": bool(xgb_clf.predict(X_preprocessed)[0]),
        "forest": bool(forest_clf.predict(X_preprocessed)[0])
    }

    # Probabilities (churn probability = class 1)
    probabilities = {
        "xgb": float(xgb_clf.predict_proba(X_preprocessed)[0][1]),
        "forest": float(forest_clf.predict_proba(X_preprocessed)[0][1])
    }

    return {
        "churn_predictions": predictions,
        "churn_probabilities": probabilities
    }

