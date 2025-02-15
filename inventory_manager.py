from inventory import Inventory
class InventoryManager:
    def __init__(self):
        self.inventory = Inventory()

    def validated_integer_input(self, prompt: str, min_value: int | None = None,
        max_value: int | None = None):
        """returns an integer that passes validation"""
        input_value = input(prompt)
        while (min_value is not None and int(input_value) > min_value or
                min_value is None) and (max_value is not None and int(input_value) < max_value
        or max_value is None) and type(input_value) == int:
            print("Invalid amount. Please re-enter:")
            input_value = input(prompt)

        return int(input_value)

    def process_command(self, command) -> bool:
        """Process user command to add items, view etc."""
        if command == 'add':
            item = input('Enter item name: ')
            quantity = self.validated_integer_input(f"How many {item} would you like to add?",
                                         1, 100)
            for x in range(quantity):
                Inventory().add_item(item)
            print("Successfully added item(s)")
            return True
        elif command == "remove":
            item = input('Enter item name: ')
            if self.inventory.is_item(item):
                quantity = self.validated_integer_input(f"How many {item} would you like to remove?",
                                                    1, 100)

                for x in range(quantity):
                    Inventory().remove_item(item)

                return True
            else:
                print("Item does not exist")
                return True

        elif command == "view":
            Inventory.view_inventory()
            return True

        elif command == "exit":
            confirmation = input("Are you sure you want to exit? (y/n) ")
            if confirmation == "y":
                return False
            else:
                return True
        else:
            print("Invalid command")
            return False

    def run(self):
        while True:
            command = input("What would you like to do (add/remove/view/exit?: ")
            if self.process_command(command):
                pass
            else:
                break







