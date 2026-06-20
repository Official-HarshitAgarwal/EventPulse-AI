# System Architecture

# 🚦 EventPulse-AI

> **Predict. Prepare. Prevent.**

---

# Overview

EventPulse-AI follows a modular, service-oriented architecture that combines Machine Learning, REST APIs, location intelligence, and AI-assisted operational decision support into a unified traffic incident management system.

The architecture is designed to be lightweight, scalable, and easy to extend for future real-time deployments.

---

# High-Level Architecture

```text
                           User

                             │

                             ▼

                 Streamlit Web Dashboard

                             │
                             │ REST API
                             ▼

                    FastAPI Backend Server

      ┌──────────────┬──────────────┬──────────────┐
      │              │              │              │
      ▼              ▼              ▼              ▼

 Random Forest   Recommendation   Emergency    Mappls API
 Prediction         Engine        Allocation  Reverse Geocode

      │              │              │              │
      └──────────────┴──────────────┴──────────────┘

                             │

                             ▼

                      JSON Response

                             │

                             ▼

               Interactive Dashboard Output
```

---

# Architecture Components

## 1. Streamlit Dashboard

The Streamlit application provides the user interface for interacting with the system.

Responsibilities:

* Collect incident information
* Send prediction requests
* Display prediction results
* Display AI recommendations
* Display emergency resources
* Display interactive map

---

## 2. FastAPI Backend

The FastAPI server acts as the central processing layer.

Responsibilities:

* Receive requests
* Validate input data
* Perform feature engineering
* Invoke ML model
* Generate recommendations
* Call Mappls API
* Allocate emergency resources
* Return structured JSON

---

## 3. Machine Learning Engine

Model Used:

**Random Forest Classifier**

Input Features include:

* Event Type
* Event Cause
* Vehicle Type
* Police Station
* Corridor
* Road Closure
* Peak Hour
* Weekend
* Month
* Day
* Event Category

Output:

* High Priority
* Low Priority
* Prediction Confidence

---

## 4. Feature Engineering Module

Transforms raw incident data into model-ready features.

Operations include:

* One-Hot Encoding
* Boolean Conversion
* Feature Alignment
* Missing Feature Handling

---

## 5. Recommendation Engine

The recommendation engine converts the prediction into actionable operational decisions.

Factors considered:

* Predicted Priority
* Peak Hour
* Road Closure
* Event Type
* Event Category
* Weekend

Outputs:

* Impact Score
* Impact Level
* Emergency Status
* Officers Required
* Barricades Required
* Diversion Requirement
* Estimated Clearance Time
* Operational Actions

---

## 6. Mappls Reverse Geocoding

Uses Mappls Reverse Geocoding API to convert GPS coordinates into readable addresses.

Input:

```
Latitude
Longitude
```

Output:

```
Formatted Address

City

State

Pincode
```

Example:

```
Kengeri Main Road
Ambedkar Circle
Bengaluru
Karnataka
560060
```

---

## 7. Emergency Resource Allocation

Provides suggested nearby emergency services.

Resources include:

* Police Station
* Hospital
* Fire Station

This enables quicker operational planning.

---

# Data Flow

```text
User submits incident

        │

        ▼

Streamlit Dashboard

        │

        ▼

POST /predict

        │

        ▼

Input Validation

        │

        ▼

Feature Engineering

        │

        ▼

Random Forest Prediction

        │

        ├────────────► Recommendation Engine

        │

        ├────────────► Emergency Allocation

        │

        └────────────► Mappls Reverse Geocoding

                     │

                     ▼

             Final JSON Response

                     │

                     ▼

          Streamlit Visualization
```

---

# Project Structure

```text
EventPulse-AI

│

├── app
│   ├── main.py
│   ├── predictor.py
│   ├── recommender.py
│   ├── emergency.py
│   ├── mappls.py
│   ├── schemas.py
│   └── utils.py
│
├── frontend
│   └── app.py
│
├── models
│   ├── random_forest.pkl
│   └── feature_columns.pkl
│
├── notebook
│
├── docs
│
├── screenshots
│
└── README.md
```

---

# Technology Stack

| Layer                | Technology                   |
| -------------------- | ---------------------------- |
| Frontend             | Streamlit                    |
| Backend              | FastAPI                      |
| Machine Learning     | Scikit-learn                 |
| Data Processing      | Pandas                       |
| Model Storage        | Joblib                       |
| Location Services    | Mappls Reverse Geocoding API |
| Programming Language | Python                       |

---

# Design Principles

The system is designed using the following principles:

* Modular Architecture
* Separation of Concerns
* RESTful API Design
* Reusable Components
* Lightweight Deployment
* Extensible ML Pipeline

Each module performs a single responsibility, making the system easier to maintain and extend.

---

# Advantages of the Architecture

* Clean separation between frontend and backend
* Fast real-time predictions
* Easy integration with external APIs
* Scalable for cloud deployment
* Supports future real-time traffic feeds
* Independent ML and recommendation modules
* Modular codebase for easier maintenance

---

# Future Architecture Enhancements

Future versions may include:

* Live Traffic API Integration
* CCTV Video Analytics
* GPS-Based Incident Detection
* Real-Time Vehicle Tracking
* Notification Services
* Cloud Deployment
* Database Integration
* User Authentication
* Admin Dashboard
* Mobile Application Support

---

# Conclusion

EventPulse-AI adopts a modular architecture that combines Machine Learning, FastAPI, Streamlit, Mappls Reverse Geocoding, and an AI-driven recommendation engine into a unified intelligent traffic incident management platform. This design enables rapid predictions, operational recommendations, and efficient emergency resource allocation while remaining scalable for future smart-city deployments.
