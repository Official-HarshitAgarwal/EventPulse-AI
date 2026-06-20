import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MAPPLS_API_KEY")


def geocode_address(address: str):

    url = "https://atlas.mappls.com/api/places/geocode"

    params = {
        "address": address,
        "access_token": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "copResults" in data and len(data["copResults"]) > 0:

        result = data["copResults"][0]

        return {
            "latitude": float(result["latitude"]),
            "longitude": float(result["longitude"])
        }

    return None