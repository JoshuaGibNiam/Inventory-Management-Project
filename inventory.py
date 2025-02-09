from item import Item
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items.update({item: Item(item, 1)})
        print("Item(s) added successfully.")


inv = Inventory()
inv.add_item("Dry-fit shirts")


