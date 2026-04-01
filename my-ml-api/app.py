#STEP 2: CREATE SIMPLE API

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import uvicorn

# Create API
app = FastAPI()

# Load model
model = joblib.load('model.pkl')

# Define what input looks like
class PredictionRequest(BaseModel):
    features: List[float]

# ONE ENDPOINT - Make prediction
@app.post("/predict")
def predict(request: PredictionRequest):
    """
    Send 30 numbers, get a prediction back!
    0 = malignant (bad)
    1 = benign (good)
    """
    # Get features from request
    features = [request.features]

 # Make prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    confidence = probability[prediction]

 
    # Return result
    return {
        "prediction": int(prediction),
        "label": "benign" if prediction == 1 else "malignant",
        "confidence": float(confidence)
    }

# Run the app
if __name__ == "__main__":
    print("🚀 Starting API on http://localhost:8000")
    print("📖 Docs at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)


    




