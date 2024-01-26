"""The Magic Inventory: Design a game inventory system where each item has a name and quantity. Use a dictionary to store the items and their quantities. Allow the player to add, remove, and view items in their inventory
"""

# add item with quantity
def add_item(inventory, item, qty):
    inventory[item] = qty

# remove item
# assuming item quantity to subract is given
# 0-quantity items will remain in inventory
def remove_item(inventory, item, qty):
    inventory[item] -= qty

def view_inventory(inventory):
    for item in inventory:
        print(f"Item: {item}, Quantity: {inventory[item]}")

# test inventory
inventory = {}

add_item(inventory, 'torch', 3)
view_inventory(inventory)
remove_item(inventory, 'torch', 1)
view_inventory(inventory)

