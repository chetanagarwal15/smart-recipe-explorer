# Smart Recipe Explorer with AI Assistance

## Project Overview
Smart Recipe Explorer is a Python backend application built using FastAPI.
It allows users to manage recipes, search and filter them based on multiple criteria,
and use Generative AI to simplify cooking instructions into easy, beginner-friendly steps.

This project is developed as part of a technical assessment for the Python AI/ML Intern role.

---

## 🛠 Tech Stack
- Backend: FastAPI (Python)
- API Documentation: Swagger UI (FastAPI auto-generated)
- AI Integration: Hugging Face Inference API (Free)
- Data Storage: In-memory Python list
- Deployment: Vercel
- Version Control: Git & GitHub

---
## Project Architecture & Approach
The application follows a modular backend architecture:

User -> FastAPI Endpoints -> Recipe CRUD (Create, Read, Update, Delete)
     -> Search & Filter -> AI Simplification -> Response

Endpoints:

POST /recipes – Add a new recipe

GET /recipes – List all recipes

GET /recipes/{id} – Get recipe by ID

PUT /recipes/{id} – Update recipe

DELETE /recipes/{id} – Delete recipe

POST /recipes/{id}/simplify – Simplify recipe instructions using AI

Flow: Users submit a recipe → Backend stores it in-memory → AI endpoint simplifies instructions (optional) → Returns formatted response.

---
## Setup Instructions (Local)

1. Clone the Repository

git clone https://github.com/chetanagarwal15/smart-recipe-explorer.git
cd smart-recipe-explorer


2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt

4. Setup Environment Variables

5. Run the Application

uvicorn main:app --reload

6. Access the APIs

Root: http://127.0.0.1:8000/

Swagger UI: http://127.0.0.1:8000/docs

---
## AI Integration Details

Model: google/flan-t5-small (Hugging Face)

Endpoint: Hugging Face Inference API

Purpose: Simplify complex recipe instructions into easy, beginner-friendly steps

Usage Example:

import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

data = {"inputs": "Boil 2 liters of water, then add pasta until soft"}
response = requests.post(API_URL, headers=headers, json=data)
simplified_text = response.json()[0]['generated_text']

## Assumptions Made

Data is stored in-memory for simplicity (no database).

Recipes follow a fixed format (title, ingredients, steps).

AI may not always return perfect results; it is for simplification guidance.

Deployment on Vercel serverless has limited Swagger UI support.

## Deployment (Vercel)

The application is deployed on Vercel as a Python serverless function.
The root endpoint is accessible and confirms successful deployment.

Note: Due to Vercel serverless limitations with FastAPI (ASGI),
Swagger UI (`/docs`) may not render correctly in production,
though all APIs work correctly when run locally.

Live URL; https://chetanagarwal15-smart-recipe-explor.vercel.app/
## How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/chetanagarwal15/smart-recipe-explorer.git
cd smart-recipe-explorer
