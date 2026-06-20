import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/random_forest.pkl")

# Load training feature columns
feature_columns = joblib.load("models/feature_columns.pkl")


def preprocess_input(data: dict):

    df = pd.DataFrame([data])

    categorical_cols = [
        "event_type",
        "event_cause",
        "authenticated",
        "veh_type",
        "corridor",
        "police_station",
        "zone",
        "junction",
        "day_of_week",
        "month",
        "event_category"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_cols
    )

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return df


def predict_priority(data: dict):

    processed_df = preprocess_input(data)

    prediction = model.predict(processed_df)[0]

    probability = model.predict_proba(processed_df)[0][1]

    return prediction, probability