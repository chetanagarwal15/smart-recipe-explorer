import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}

def simplify_recipe(instructions: str):
    payload = {
        "inputs": f"Simplify this recipe in easy steps: {instructions}"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
