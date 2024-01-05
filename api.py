# To run open terminal and type the following:
# uvicorn API:app --reload

import Product
from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: Product.Product('Whole Milk', 3.99, 'Borden').__str__,
    2: Product.Product('Fat Free Milk', 4.99, 'Borden').__str__
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
