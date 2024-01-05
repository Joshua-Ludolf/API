class Product:
    def __init__(self, name: str, price: float, brand: str):
        self.name = name
        self.price = price
        self.brand = brand

    @property
    def __getattr__(self):
        return {self.name}, {self.price}, {self.brand}

    @property
    def __str__(self):
        return f'{self.__getattr__}'
