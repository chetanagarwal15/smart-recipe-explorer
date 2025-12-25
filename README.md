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
## Deployment (Vercel)

The application is deployed on Vercel as a Python serverless function.
The root endpoint is accessible and confirms successful deployment.

Note: Due to Vercel serverless limitations with FastAPI (ASGI),
Swagger UI (`/docs`) may not render correctly in production,
though all APIs work correctly when run locally.

## ⚙️ How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/chetanagarwal15/smart-recipe-explorer.git
cd smart-recipe-explorer
