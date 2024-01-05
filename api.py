# To run open terminal and type the following:
# uvicorn API:app --reload

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
        inventory_list += i + '\n'
    return f'{inventory_list}'


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="The ID of the item you would like to view.")):
    return inventory[item_id]
