"""
config.py
Loads environment variables and creates a shared OpenAI client.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ----------------------------------------------------
# Load .env variables
# ----------------------------------------------------
load_dotenv()

# ----------------------------------------------------
# API Keys
# ----------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

# ----------------------------------------------------
# Validate API Keys
# ----------------------------------------------------
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. Please add it to your .env file."
    )
if not NEWSDATA_API_KEY:
    raise ValueError(
        "NEWSDATA_API_KEY not found. Please add it to your .env file."
    )

# ----------------------------------------------------
# Shared OpenAI Client (import this everywhere else)
# ----------------------------------------------------
client = OpenAI(api_key=OPENAI_API_KEY)