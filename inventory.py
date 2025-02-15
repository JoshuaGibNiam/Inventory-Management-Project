from item import Item
class Inventory:
    def __init__(self):
        self.items = {}

    def is_item(self, item):
        if item in self.items:
            return True
        else:
            return False
    def add_item(self, item: str):
        if item in self.items:
            self.items[item].quantity += 1
        else:
            self.items.update({item: Item(item, 1)})


    def remove_item(self, item: str, quantity: int):
        if item in self.items:
            self.items[item].quantity -= quantity
            if self.items[item].quantity <= 0:
                del self.items[item]
        else:
            print("Item not found")

    def view_inventory(self):
        if self.items:
            for name, item in self.items.items():
                print(f"{name}: {item.quantity}")
            print("End of inventory. \n")
        else:
            print("Inventory is empty.")



