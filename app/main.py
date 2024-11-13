from fastapi import FastAPI
from app.routes import greeting
from dotenv import load_dotenv

load_dotenv("../.env")

app = FastAPI()

app.include_router(greeting.greeting_router)