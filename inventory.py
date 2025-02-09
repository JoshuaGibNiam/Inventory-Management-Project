from item import Item
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str):
        if item in self.items:
            self.items[item].quantity += 1
        else:
            self.items.update({item: Item(item, 1)})
        print("Item(s) added successfully.")

    def remove_item(self, item: str, quantity: int):
        if item in self.items:
            self.items[item].quantity -= quantity
            if self.items[item].quantity <= 0:
                del self.items[item]
            print("Item(s) removed successfully.")
        else:
            print("Item not found")

    def report_items(self):
        pass


inv = Inventory()
inv.add_item("Dry-fit shirts")
inv.add_item("Dry-fit shirts")
inv.remove_item("Dry-fit shirts", 1)


