# shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def __repr__(self):
        return f"Shoe('{self.brand}', {self.size})"
