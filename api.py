# To run open terminal and type the following:
# uvicorn api:app --reload

import product
from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: product.Product('Whole Milk', 3.99, 'Borden').__str__,
    2: product.Product('Fat Free Milk', 4.99, 'Borden').__str__
}


@app.get("/")
def home():
    inventory_list = ''
    for key, i in inventory.items():
        inventory_list += i + "\n"
    return f'{inventory_list}'  # JSON format = python dictionary


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="ID of Item")):
    return inventory[item_id]
