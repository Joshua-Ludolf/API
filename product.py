from typing import Optional

class Item():
    def __init__(self, name: str, price: float, brand: Optional[str]):
        self.name = name
        self.price = price
        self.brand = brand

inventory = {
    
    1: {
            'name' : 'Whole Milk', 
            'price' : '$' + str(3.99), 
            'brand' : 'Borden' 
        },

    2: {
            'name' : 'Fat Free Milk',
            'price' : '$' + str(4.99),
            'brand' : 'Borden'
       }

    }
