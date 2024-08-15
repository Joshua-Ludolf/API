# To run open terminal and type the following:
# uvicorn api:app --reload

from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
import uvicorn
from pydantic import BaseModel
import json


class Item(BaseModel):
    name: str
    price: str
    brand: str



app = FastAPI()


@app.get("/")
def home():
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        inventory = {}
    return inventory
    

@app.get('/get-item/{item_id}')
def get_item(item_id: str = Path(description="ID of Item")):
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        inventory = {}
    if inventory.get(item_id) is None:
        return {"Item Doesn't Exist!"}
    return inventory.get(item_id)


@app.put('/add-product')
async def add_item(item: Item):
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        inventory = {}
    new_key = len(inventory) + 1
    inventory[new_key] = item.dict()

    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)
    file.close()
    return {"inventory": inventory}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    