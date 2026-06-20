import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MAPPLS_API_KEY")


def reverse_geocode(lat, lng):

    url = "https://search.mappls.com/search/address/rev-geocode"

    params = {
        "access_token": API_KEY,
        "lat": lat,
        "lng": lng
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["responseCode"] == 200:
        return data["results"][0]

    return {}