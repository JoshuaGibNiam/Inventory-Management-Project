import item
from item import Item
import json
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

    def load_inventory(self):
        """load inventory from json file. If file does not exist (first time users),
        Create a json file."""
        try:
            with open('.venv/inventory.json', 'r') as file:
                self.items = json.load(file)
                self.to_item()#load items to inventory
        except (FileNotFoundError, json.JSONDecodeError):
            with open('.venv/inventory.json', 'a') as file:
                self.items = {} #inventory remains empty

    def save_inventory(self):
        self.to_dict()
        with open('.venv/inventory.json', 'w') as file:
            json.dump(self.items, file)

    def to_dict(self):
        self.items = {key: {"name": item.name, "quantity": item.quantity}
                      for key, item in self.items.items()}

    def to_item(self):
        self.items = {key: Item(item["name"], item["quantity"])
                      for key, item in self.items.items()}

    def rename_item(self, old_name, new_name):
        quantity = self.items[old_name].quantity
        del self.items[old_name]
        self.items.update({new_name: Item(new_name, quantity)})








