# Your Task
# Design and implement a ShoppingCart class that can hold multiple items. Each item in the shopping cart should be represented 
# as instances of an Item class, which contains name and price attributes.

# Your ShoppingCart class should allow adding items, removing items, and calculating the total cost of the cart.

# Example Usage
# Your classes should be usable as follows:

# cart = ShoppingCart()
# cart.add_item(Item(name="Milk", price=3.50))
# cart.add_item(Item(name="Eggs", price=2.00))
# cart.add_item(Item(name="Bread", price=2.50))

# print(cart.total_cost())  # Expected output: 8.0

# cart.remove_item("Eggs")
# print(cart.total_cost())  # Expected output: 6.0
# Guidelines
# Implement the Item class with __init__ method to initialize name and price.
# The ShoppingCart class should include methods for add_item, remove_item, and total_cost.
# add_item: Accepts an Item instance and adds it to the cart.
# remove_item: Accepts an item name, searches for the item in the cart, and removes it if found. If multiple items in the cart have the 
# same name, remove only the first one.
# total_cost: Calculates and returns the total price of all items in the cart.
# Ensure that your ShoppingCart can handle multiple items with the same name correctly.
# Consider how to store items within the ShoppingCart class for efficient addition, removal, and total cost calculation.

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break

    def total_cost(self):
        return sum(item.price for item in self.items)
    
cart = ShoppingCart()
cart.add_item(Item(name="Milk", price=3.50))
cart.add_item(Item(name="Eggs", price=2.00))
cart.add_item(Item(name="Bread", price=2.50))
print(cart.total_cost())

cart.remove_item("Eggs")
print(cart.total_cost())