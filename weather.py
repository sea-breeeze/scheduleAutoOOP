import requests
import streamlit as st

@st.cache_data(ttl=600)

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 35.4676,
        "longitude": -97.5164,
        "current": "temperature_2m,relative_humidity_2m",
        "temperature_unit": "fahrenheit",
        "timezone": "America/Chicago"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data["current"] 