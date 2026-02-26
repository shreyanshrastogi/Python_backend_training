from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
inventory = {}


class Item(BaseModel):
    item: str
    quantity: int
    price: float


@app.post("/inventory/add/{item_id}")
def add_item(item_data: Item, item_id: int):
    if item_id in inventory:
        raise HTTPException(status_code=409, detail="item already present")
    inventory[item_id] = item_data
    return {"message": "added", "item": inventory[item_id]}


@app.get("/inventory/check/{item_id}")
def check_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item not present")
    return inventory[item_id]


@app.put("/inventory/update/{item_id}")
def update_item(item_data: Item, item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item not present")
    inventory[item_id] = item_data
    return {"message": "updated", "item": inventory[item_id]}


@app.delete("/inventory/delete/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item not present")
    del inventory[item_id]
    return {"message": f"{item_id} deleted successfully"}
