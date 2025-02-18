# Inventory Management Program
This is a program helps you store data to an inventory. You can add anything, from clothes
to shopping lists, to the inventory, which will automatically save after exiting the program.

---

## Features
1. **Adding items**: Add items to your inventory. State its name, and the quantity that you have.
2. **Remove items**: Remove items from your inventory. State the name of the item you desire to remove, 
and how much of it you want to remove.
3. **View inventory**: Prints out the items and quantities available in your inventory.
4. **Rename an item**: Rename an item (if you made a mistake typing its name before). State
its original name, and the new name you want to give it.
5. **Exit**: The program will ask for a confirmation, then proceed to log changes made to 
the inventory, before closing the program.
6. **Logging**: When starting the program, it will open up a file and load the data
to your inventory. For first-time users, it will automatically create an empty file.
When exiting, the program will automatically save changes made to the inventory into the file.
7. **String and integer validation**: Ensures inputs are valid. If not, the user will have to re-enter.

---

## Usage
This program is pretty self-explanatory. Invalid inputs will be ignored.
**Important note**: Exit the program by **typing "exit" as a command**, not manually closing the program.
Doing so will not save changes made to the inventory.

---

## Code
This program consists of 3 classes, each in a separate file.
1. item.py: *Item* class creates an Item object, which will be used in the Inventory class.
2. inventory.py: *Inventory* class consists of all the functions of this program, a bit like the back-end of this program.
3. inventory_manager.py: *InventoryManager* class handles user commands, a bit like the front-end of this program.
4. main.py: Where the program will be run directly.

---
Sunday, 16th of February 2025, 12:14 p.m.