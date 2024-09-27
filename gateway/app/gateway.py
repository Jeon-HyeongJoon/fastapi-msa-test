# gateway.py
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "API Gateway"}
    
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    response = requests.get(f"http://user-service:8000/users/{user_id}")
    return response.json()

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    response = requests.get(f"http://order-service:8000/orders/{order_id}")
    return response.json()