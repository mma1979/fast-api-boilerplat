
from fastapi import FastAPI, APIRouter
import os

greeting_router = APIRouter(prefix='/api/v1/greeting', tags=['Greeting'])

@greeting_router.get('/')
async def welcome():
     return {
        "message": "Hello World!"
    }

@greeting_router.get('/info')
async def get_info():
     return {
          "APP_NAME": os.getenv("APP_NAME", "NO_NAME"),
          "APP_VERSION":  os.getenv("APP_VERSION", "NO_VERSION")
     }
