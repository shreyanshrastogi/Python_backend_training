from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
inventory = {}


class Item(BaseModel):
    item_id: int
    item: str
    quantity: int
    price: float


@app.post("/inventory/add")
def add_item(item_data: Item):
    if item_data.item_id in inventory:
        raise HTTPException(status_code=404, detail="item already present")
    inventory[item_data.item_id] = {}
    inventory[item_data.item_id]["item"] = item_data.item
    inventory[item_data.item_id]["quantity"] = item_data.quantity
    inventory[item_data.item_id]["price"] = item_data.price
    return inventory


@app.get("/inventory/check/{item_id}")
def check_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=409, detail="item not present")
    return inventory[item_id]


@app.put("/inventory/update/{item_id}")
def update_item(item_id: int, item_data: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item not present")
    inventory[item_id]["item"] = item_data.item
    inventory[item_id]["quantity"] = item_data.quantity
    inventory[item_id]["price"] = item_data.price


@app.delete("/inventory/delete/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item not present")
    del inventory[item_id]
