# How LLM's interact with outside world.

    # Can ChatGPT tell todays wether ?

    # LLMS are excellent at generating text, images and other content.
    # but they can not perform actions unless connected to external tools.

        # Agoda.
        # MMT.

        # MMT
        # Lemon Tree
        # Mustache
        # Airbnb


# Agent:- -> 
            # Program that has access to different platforms.
            # Which chooses best option
            # and provides service to us.


# Why do we need AI Agents:

    # User --> LLM ---> Answer

    # User --> LLM --> Tool --> Internet / API --> LLM -> Answer

# Wether info  => Google Wether
# Jokes        => Jokesnow
# book ticket  => MMT

#-----------------------------------------

    # ChatGPT
    # Github Copilot
    # Cursor AI
# --------------------------------------------------------------

#Normal:
# User  --> LLM --> Text

# Function Calling:
# User --> LLM --> Function --> Python --> LLM --> Response
# What is the wethere in hyderabad?

# LLM

# Function --> API


# response = {
#     "temperature": 30,
#     "condition": "sunny"
# }

#LLM

# Todays wethere in hyderabad is sunny with a temperature of 30 C


# import requests

# city = "Jaipur"

# geo = requests.get(
#     "https://geocoding-api.open-meteo.com/v1/search",
#     params={"name": city, "count": 1}
# ).json()

# location = geo["results"][0]

# weather = requests.get(
#     "https://api.open-meteo.com/v1/forecast",
#     params={
#         "latitude": location["latitude"],
#         "longitude": location["longitude"],
#         "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
#     }
# ).json()

# print(weather["current"])
#-----------------------------------------------------

from openai import OpenAI
import base64
import os
from dotenv import load_dotenv
load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=API_KEY)

# result = client.images.generate(
#     model="gpt-image-1",
#     prompt="A nano banana dish in a fancy restaurant with a futuristic AI theme"
# )

# image_bytes = base64.b64decode(result.data[0].b64_json)

# with open("image.png", "wb") as f:
#     f.write(image_bytes)

import requests

API_KEY = os.getenv("NEWSDATA_API_KEY")

url = "https://newsdata.io/api/1/latest"

params = {
    "apikey": API_KEY,
    "country": "in",
    "language": "en",
    "category": "technology"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())