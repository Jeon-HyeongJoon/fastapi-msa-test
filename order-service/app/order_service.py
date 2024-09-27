# order_service.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Order Service"}

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    return {"order_id": order_id, "status": "pending"}