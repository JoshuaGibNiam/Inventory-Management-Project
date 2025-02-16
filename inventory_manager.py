from inventory import Inventory
class InventoryManager:
    def __init__(self):
        self.inventory = Inventory()
    def is_valid_string(self, string):
        if string.isspace() or len(string) == 0:
            print("Invalid name. Please re-enter.")
            return False
        else:
            return True
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
        if command == '1' or command == "add": #add
            item = input('Enter item name: ')
            while not self.is_valid_string(item):
                item = input("Enter item name: ")
            quantity = self.validated_integer_input(f"How many {item}(s) would you like to add?",
                                         1, 100)
            for x in range(quantity):
                self.inventory.add_item(item)
            print("Successfully added item(s)")
            return True

        elif command == "2" or command == "remove": #remove
            item = input('Enter item name: ')
            if self.inventory.is_item(item):
                quantity = self.validated_integer_input(f"How many {item}(s) would you like to remove?",
                                                    1, 100)

                for x in range(quantity):
                    self.inventory.remove_item(item)

                return True
            else:
                print("Item does not exist")
                return True

        elif command == "3" or command == "view": #view
            self.inventory.view_inventory()
            return True

        elif command == "4" or command == "rename":
            oldname = input("Enter the item's original name: ")
            if not self.inventory.is_item(oldname):
                print("Item does not exist.")
                return True
            newname = input("Enter the new name: ")
            if not self.is_valid_string(newname):
                newname = input("Enter new name: ")
            self.inventory.rename_item(oldname, newname)
            print("Successfully renamed item")
            return True

        elif command == "5" or command == "exit": # exit
            confirmation = input("Are you sure you want to exit? (y/n): ")
            if confirmation == "y":
                self.inventory.save_inventory()
                print("Inventory saved")
                return False
            else:
                return True
        else:
            print("Invalid command")
            return True

    def run(self):
        self.inventory.load_inventory()
        while True:
            print('\n\n')
            command = input("What would you like to do?\n"
                            "To add an item, enter {1}\n"
                            "To remove an item, enter {2}\n"
                            "To view all items, enter {3}\n"
                            "To rename an item, enter {4}\n"
                            "To exit, enter {5}\n"
                            "Enter (1-5):")
            print("\n\n")
            if self.process_command(command):
                pass
            else:
                break







