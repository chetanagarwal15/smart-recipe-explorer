from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Smart Recipe Explorer")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FastAPI running on Vercel"}
