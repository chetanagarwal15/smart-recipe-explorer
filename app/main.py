from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Smart Recipe Explorer")

app.include_router(router)
