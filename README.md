# 📉 Churn Detection API

A customer churn prediction service using **XGBoost** and **Random Forest**.  
Given customer attributes, the API returns whether the customer will churn and the probabilities from both models.

---
```
## 🗂️ Repository Structure
```bash
churn-detection/
├── utils/
│ ├── config.py # configuration paths, constants
│ ├── validation.py # Pydantic model definitions (CustomerData)
│ └── prediction.py # function that loads models & returns predictions
├── main.py # FastAPI entrypoint
├── requirements.txt # Python dependencies
├── models/ or artifacts/ # (should contain saved model files & preprocessor)
├── data/ # (optional) raw / processed datasets
└── README.md
```
```
---

## 🧠 How It Works

1. **Input**: JSON object containing customer features.  
2. **Validation**: Pydantic `CustomerData` ensures data is properly typed and within valid ranges.  
3. **Preprocessing**: Loaded `ColumnTransformer` preprocesses input to the same format used during training.  
4. **Prediction**: Two models (XGB and Random Forest) are loaded from disk; they output churn label and probability.  
5. **Output**: JSON with labels (`true` / `false`) and probabilities for both models.

---

## 📥 Example Input & Output

### Input

```json
{
  "CreditScore": 0,
  "Geography": "Germany",
  "Gender": "Male",
  "Age": 18,
  "Tenure": 10,
  "Balance": 0,
  "NumOfProducts": 1,
  "HasCrCard": 0,
  "IsActiveMember": 0,
  "EstimatedSalary": 0
}
 ```

### Output
```json
{
  "churn_predictions": {
    "xgb": false,
    "forest": false
  },
  "churn_probabilities": {
    "xgb": 0.41689127683639526,
    "forest": 0.38248286818369204
  }
}
```
## 🔌 API Endpoints & Authentication
### GET /

* Health check: returns a simple welcome message.

### POST /predictions

* Requires header: X-API-Key: <your_secret_token>

* Body: JSON matching CustomerData.

* Returns predictions and probabilities as shown above.

## 🛠 Installation & Running
```bash
git clone https://github.com/Zeyadelgabbas/churn-detection.git
cd churn-detection
python -m venv venv
# Activate venv:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```
### Run the API:
```bash
uvicorn main:app --reload
```
Visit Swagger UI at:
http://127.0.0.1:8000/docs

## 🔑 Authentication

This API requires an **API Key** for authentication.

1. Create a `.env` file in the root of your project and add the following:

```env
SECRET_KEY_TOKEN=your_secret_token_here
```

## 📈 Model Details & Notes

Uses XGBoost and RandomForest for classification.

Preprocessing ensures input data matches training format (scaling, encoding, etc.).

The predictions are based on the probability of the positive class (churn).

## 🚧 Future Improvements

Add model interpretability (SHAP/LIME) to explain why a customer might churn.

Add more robust input validation and error handling.

Add logging, monitoring, and CI/CD for deployment.

Support batch predictions (multiple customers in one request).

Optionally add a front-end or UI for non-technical users.
