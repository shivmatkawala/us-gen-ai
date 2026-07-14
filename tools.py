import os
import uuid
import base64
import requests

from config import client, NEWSDATA_API_KEY


# ====================================================
# TOOL 1 : WEATHER
# ====================================================
def get_weather(city):
    """
    Returns current weather for a city using Open-Meteo API.
    """
    try:
        # Step 1 : Convert city -> latitude & longitude
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1
            },
            timeout=10
        ).json()

        if not geo.get("results"):
            return {
                "error": f"City '{city}' not found."
            }

        location = geo["results"][0]

        # Step 2 : Fetch Weather
        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
            },
            timeout=10
        ).json()

        current = weather["current"]

        return {
            "city": city,
            "temperature_c": current["temperature_2m"],
            "humidity_percent": current["relative_humidity_2m"],
            "wind_speed_kmh": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# ====================================================
# TOOL 2 : NEWS
# ====================================================
def get_news(category="technology"):
    """
    Returns latest news headlines.
    """
    try:
        url = "https://newsdata.io/api/1/latest"
        params = {
            "apikey": NEWSDATA_API_KEY,
            "country": "in",
            "language": "en",
            "category": category
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("status") != "success" or not data.get("results"):
            return {
                "error": f"No news found for category '{category}'."
            }

        news = []
        for article in data["results"][:5]:
            news.append({
                "title": article.get("title"),
                "source": article.get("source_name"),
                "link": article.get("link")
            })

        return news

    except Exception as e:
        return {
            "error": str(e)
        }


# ====================================================
# TOOL 3 : IMAGE GENERATION
# ====================================================
def generate_image(prompt):
    """
    Generates an image using GPT Image Model.
    """
    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt
        )

        image_bytes = base64.b64decode(result.data[0].b64_json)

        os.makedirs("generated_images", exist_ok=True)
        filename = f"{uuid.uuid4().hex}.png"
        filepath = os.path.join("generated_images", filename)

        with open(filepath, "wb") as image_file:
            image_file.write(image_bytes)

        return {
            "status": "success",
            "message": "Image generated successfully.",
            "image_path": filepath
        }

    except Exception as e:
        return {
            "error": str(e)
        }