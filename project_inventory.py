''' Create an application which manages an inventory of products.
 Create a product class which has a price, id, and quantity on hand. 
 Then create an inventory class which keeps track of various products 
 and can sum up the inventory value.'''


class Inventory():

    items_in_inventory = {}
    
    def __init__(self, inventory_name):
        self.inventory_name = inventory_name

    def add_item(self, product, price, quantity):
        
        # Add product to the inventory        
        if not product in self.items_in_inventory:
            self.items_in_inventory[product] = (price, quantity)
            print product + " added."
        else:
            print product + " is already in the inventory."

        print
                
    def remove_item(self, product):
        """Remove product from the inventory."""
        if product in self.items_in_inventory:
            del self.items_in_inventory[product]
            print product + " removed."
        else:
            print product + " is not in the inventory."
        print
        
    def print_inventory(self):
        
        print self.items_in_inventory
        print
            
    def prompt(self):
        
        i = raw_input('New item(+), remove item(-) or print cart(=): ')
    
        if i == '+':
            name = raw_input('NAME: ')
            cost = raw_input('PRICE: ')
            quant = raw_input('QUANT: ')         
            
            inventory.add_item(name, float(cost), int(quant))
        
        elif i == '-':
            name = raw_input('NAME: ')
            inventory.remove_item(name)
            
        elif i == '=':
            inventory.print_inventory()
            
        inventory.prompt()

inventory_name = raw_input('Inventory name: ')
inventory = Inventory(inventory_name)

inventory.prompt()