"""The Legendary Inventory: Design a game inventory system where the player can add or remove items
   from their inventory. Use lists to store the items and allow the player to perform actions such as
   viewing, adding, or dropping items.
"""

# add item
def add_item(inventory, item):
    inventory.append(item)

# view item
def view_inventory(inventory):
    for item in inventory:
        print(item)

# drop items
def drop_item(inventory, item):
    inventory.remove(item)

# test
# note this would be better as an inventory class
inventory = []
add_item(inventory, 'torch')
add_item(inventory,'sword')
add_item(inventory, 'old shoe')

view_inventory(inventory)
drop_item(inventory, 'old shoe')
view_inventory(inventory)
