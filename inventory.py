# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    
    for k, v in inventory.items():
        print(str(v), k)
        item_total = item_total + v
    
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    
    for i in addedItems:
        if i not in inventory:
            inventory.setdefault(i, 1)
        else:
            inventory[i] = inventory.get(i, 0) + 1
        
    return inventory
        #inventory[i] = inventory[i].values() + 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)