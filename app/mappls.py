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

    print("MAPPLS STATUS:", response.status_code)
    print("MAPPLS RAW RESPONSE TEXT:", response.text)

    try:
        data = response.json()
    except ValueError:
        print("MAPPLS ERROR: response was not valid JSON")
        return {}

    print("MAPPLS PARSED RESPONSE:", data)

    if data.get("responseCode") == 200:
        return data["results"][0]

    return {}
