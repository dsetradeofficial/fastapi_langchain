from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description


app = FastAPI()

class Order(BaseModel):
    product:str
    units:int

class Product(BaseModel):
    name:str
    notes:str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name:str = 'world'):
    return {"message": f"hello {name}"}

@app.post("/orders")
async def place_order(product:str,units:int):
    return {"message": f"Order for {units} of {product} placed successfully"}

@app.post("/orders_pyddantic")
async def place_order(order:Order):
    return {"message": f"Order for {order.units} of {order.product} placed successfully"}

@app.post("/product_description")
async def generate_product_description(product:Product):
    description = generate_description(f"Product name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}
