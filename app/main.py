from fastapi import FastAPI

from app.schemas import EventData
from app.predictor import predict_priority
from app.recommender import generate_recommendation
from app.mappls import reverse_geocode
from app.emergency import get_emergency_resources

app = FastAPI(
    title="EventPulse-AI API",
    description="Traffic Event Priority Prediction API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "EventPulse-AI",
        "status": "Running Successfully 🚀"
    }


@app.post("/predict")
def predict(event: EventData):

    prediction, probability = predict_priority(
        event.model_dump()
    )

    predicted_priority = "High" if prediction == 1 else "Low"

    recommendation = generate_recommendation(
        event.model_dump(),
        predicted_priority
    )

    location = reverse_geocode(
        event.latitude,
        event.longitude
    )

    resources = get_emergency_resources(
        event.police_station
    )

    return {
        "predicted_priority": predicted_priority,
        "confidence": round(probability * 100, 2),
        "location": location,
        "recommendation": recommendation,
        "resources": resources
    }