# To run open terminal and type the following:
# uvicorn api:app --reload

import product
from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: product.Product('Whole Milk', 3.99, 'Borden'),
    2: product.Product('Fat Free Milk', 4.99, 'Borden')
}

inventory_list = []

for key in inventory:
    inventory_list.append(inventory[key])


@app.get("/")
def home():
    return {'Inventory': f'{inventory_list}'}  # JSON format = python dictionary


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="The ID of the item you would like to view.")):
    return inventory[item_id]
