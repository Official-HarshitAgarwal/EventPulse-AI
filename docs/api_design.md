# API Design Document

# 🚦 EventPulse-AI

> **Predict. Prepare. Prevent.**

---

# Overview

EventPulse-AI provides a RESTful API built with **FastAPI** for intelligent traffic incident management. The API predicts incident priority using a Machine Learning model, converts geographic coordinates into human-readable locations using Mappls Reverse Geocoding, generates AI-powered response recommendations, and allocates emergency resources.

---

# Technology Stack

| Component        | Technology                   |
| ---------------- | ---------------------------- |
| Backend          | FastAPI                      |
| Machine Learning | Scikit-learn                 |
| Data Processing  | Pandas, NumPy                |
| API Validation   | Pydantic                     |
| Model Loading    | Joblib                       |
| Geolocation      | Mappls Reverse Geocoding API |

---

# Base URL

```
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Architecture

```
                Client

                   │

                   ▼

          POST /predict

                   │

                   ▼

         Request Validation

                   │

                   ▼

       Feature Engineering

                   │

                   ▼

   Random Forest Prediction

                   │

        ┌──────────┴──────────┐

        ▼                     ▼

 Mappls Reverse         Recommendation
    Geocoding               Engine

        │                     │

        └──────────┬──────────┘

                   ▼

     Emergency Resource Engine

                   │

                   ▼

             JSON Response
```

---

# Available Endpoints

| Method | Endpoint | Description                       |
| ------ | -------- | --------------------------------- |
| GET    | /        | Health Check                      |
| POST   | /predict | Predict traffic incident priority |

---

# Health Check

## Endpoint

```
GET /
```

### Response

```json
{
  "message": "EventPulse-AI API is running"
}
```

---

# Predict Incident

## Endpoint

```
POST /predict
```

---

# Request Body

```json
{
  "latitude": 12.9328703,
  "longitude": 77.4879814,
  "event_type": "unplanned",
  "event_cause": "vehicle_breakdown",
  "authenticated": "yes",
  "veh_type": "bmtc_bus",
  "police_station": "Kengeri",
  "zone": "Unknown",
  "junction": "Unknown",
  "corridor": "Non-corridor",
  "requires_road_closure": false,
  "hour": 7,
  "day_of_week": "Tuesday",
  "month": "January",
  "is_weekend": false,
  "is_peak_hour": true,
  "event_category": "Incident"
}
```

---

# Request Parameters

| Parameter             | Type    | Description                      |
| --------------------- | ------- | -------------------------------- |
| latitude              | float   | Incident latitude                |
| longitude             | float   | Incident longitude               |
| event_type            | string  | Planned or Unplanned             |
| event_cause           | string  | Cause of incident                |
| authenticated         | string  | Event verification status        |
| veh_type              | string  | Vehicle involved                 |
| police_station        | string  | Nearest police station           |
| zone                  | string  | Traffic zone                     |
| junction              | string  | Nearby junction                  |
| corridor              | string  | Corridor type                    |
| requires_road_closure | boolean | Whether road closure is required |
| hour                  | integer | Hour of incident                 |
| day_of_week           | string  | Day of week                      |
| month                 | string  | Month                            |
| is_weekend            | boolean | Weekend flag                     |
| is_peak_hour          | boolean | Peak hour flag                   |
| event_category        | string  | Incident category                |

---

# Sample Response

```json
{
  "predicted_priority": "High",

  "confidence": 94.72,

  "location": {
    "formatted_address": "Kengeri Main Road, Ambedkar Circle, Bengaluru, Karnataka"
  },

  "recommendation": {

    "impact_score": 90,

    "impact_level": "High",

    "emergency_status": "Immediate Response",

    "officers_required": 8,

    "barricades_required": 6,

    "diversion_required": true,

    "estimated_clearance_time": "45 Minutes",

    "actions": [
      "Dispatch traffic officers immediately",
      "Deploy barricades",
      "Enable traffic diversion",
      "Notify emergency services"
    ]
  },

  "resources": {

    "police": "Kengeri Police Station",

    "hospital": "Rajarajeshwari Hospital",

    "fire_station": "Kengeri Fire Station"

  }
}
```

---

# API Workflow

1. Receive incident information.
2. Validate request using Pydantic.
3. Perform feature engineering.
4. Generate priority prediction using the Random Forest model.
5. Reverse geocode coordinates using Mappls API.
6. Generate AI response recommendations.
7. Allocate emergency resources.
8. Return a structured JSON response.

---

# Machine Learning Integration

The prediction engine uses a trained **Random Forest Classifier**.

Model artifacts:

* `random_forest.pkl`
* `feature_columns.pkl`

The backend loads these models during startup and performs real-time inference for every request.

---

# Recommendation Engine

The recommendation engine analyzes:

* Predicted Priority
* Peak Hour
* Road Closure
* Event Category
* Event Type
* Weekend Status

It generates:

* Impact Score
* Impact Level
* Emergency Status
* Officers Required
* Barricades Required
* Diversion Recommendation
* Estimated Clearance Time
* Operational Action List

---

# Reverse Geocoding

The API integrates with **Mappls Reverse Geocoding API** to convert GPS coordinates into human-readable addresses.

Example:

```
Latitude:
12.9328703

Longitude:
77.4879814

↓

Kengeri Main Road,
Ambedkar Circle,
Bengaluru,
Karnataka
```

---

# Emergency Resource Allocation

Based on the predicted incident severity, the API recommends:

* 🚓 Nearest Police Station
* 🏥 Nearby Hospital
* 🚒 Fire Station

This assists authorities in making faster operational decisions.

---

# Status Codes

| Status Code | Description           |
| ----------- | --------------------- |
| 200         | Request Successful    |
| 400         | Bad Request           |
| 422         | Validation Error      |
| 500         | Internal Server Error |

---

# Security

Current implementation:

* Input validation using Pydantic
* Structured JSON responses
* RESTful API architecture

Future improvements:

* JWT Authentication
* API Key Authentication
* HTTPS Deployment
* Rate Limiting
* OAuth Integration

---

# Performance

Typical request execution:

| Stage               | Operation          |
| ------------------- | ------------------ |
| Validation          | Pydantic           |
| Feature Engineering | Data preprocessing |
| Prediction          | Random Forest      |
| Reverse Geocoding   | Mappls API         |
| Recommendation      | AI Rule Engine     |
| Resource Allocation | Rule-based Engine  |

Average response time:

**< 1 second** (excluding external API latency).

---

# Future Enhancements

* Real-time Traffic API Integration
* CCTV Video Analytics
* Batch Prediction API
* Route Optimization
* Historical Analytics
* Emergency Vehicle Tracking
* Notification Service
* Cloud Deployment

---

# Conclusion

EventPulse-AI provides a unified REST API for intelligent traffic incident management by combining Machine Learning, location intelligence, AI-assisted recommendations, and emergency resource allocation into a single, easy-to-use service. The API is designed to support rapid operational decision-making and improve response efficiency during traffic incidents.
