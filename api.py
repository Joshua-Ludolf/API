# To run open terminal and type the following:
# uvicorn api:app --reload

from typing import Optional
import product
from fastapi import FastAPI, Path, Query, HTTPException


app = FastAPI()


@app.get("/")
def home():
    inventory_list = []
    for i in product.inventory.values():
        inventory_list.append(i)
    return inventory_list

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description="ID of Item")):
    item = '{' + product.inventory.get(item_id).__getitem__('name') + ', ' + product.inventory.get(item_id).__getitem__('price') +', ' + product.inventory.get(item_id).__getitem__('brand') + '}'
    return item

@app.get('/get-price/{name}')
def get_item(name: Optional[str] = None):
    for i in product.inventory:
        if product.inventory[i]['name'] == name:
            return product.inventory.get(i).__getitem__('price')
    return{'Data': 'Not found!'}

@app.get('/brand/{brand_name}')
def get_items(brand_name: Optional[str] = None):
    products = []
    for i in product.inventory:
        if product.inventory[i]['brand'] == brand_name:
            products.append(product.inventory[i].__getitem__('name') + ', ' + product.inventory[i].__getitem__('price'))
    return products


    
