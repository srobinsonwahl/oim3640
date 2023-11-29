"""
*Exercise 05* (group work)
Write a definition for a class of anything you want. You have to use the following methods:

init method that initializes some attributes. One of the attributes has to be an empty list.

str method that returns a string that reasonably represent the thing.

A special method that overloads the one type of operators.

Some other methods that reasonably represent the thing's actions, inclduing one method that takes an object of any type and adds it to the attribute of type list.

Test your code by creating two objects and using all the methods.

Shopping cart
list of multiple items

"""

class Cart:
    """
    represents a shopping cart in the grocery store
    attr: item quantity, item name, 
    """


    def __init__(self):
        """
        attributes of cart
        """
        self.items = []


    def __str__(self):
        """
        returns cart in human readable form
        """
        cart_str = f'The cart contains {len(self.items)} different items:\n'
        for item, quantity in self.items:
            cart_str += f'Item: {item}, Quantity: {quantity}\n'
        return cart_str.strip()
    

    def __add__(self, other):
        """
        overloads the + operator
        """
        new_cart = Cart()

        for item, quantity in self.items:
            new_cart.buy_item(item, quantity)
        
        for item, quantity in other.items:
            new_cart.buy_item(item, quantity)

        return new_cart
    

    def buy_item(self, item_name, quantity=1):
        """
        returns new cart with added item name and quantity
        """
        for i, (item, item_quantity) in enumerate(self.items):
            if item == item_name:
                self.items[i] = (item, item_quantity + quantity)
                break
        else:
            self.items.append((item_name, quantity))

    
    def remove_item(self, item_name, quantity=1):
        """
        returns a new cart with subtracted item name and quantity
        """
        for i, (item, item_quantity) in enumerate(self.items):
            if item == item_name:
                new_quantity = item_quantity - quantity
                if new_quantity > 0:
                    self.items[i] = (item, new_quantity)
                else:
                    del self.items[i]
                break

"""
OBJECT 1 TEST CODE:
"""
# Test __init__ method with cart 1:
# Test __str__ method with cart 1:
# Test buy_item method with cart1:
# Test remove_item method with cart1:
cart1 = Cart()
cart1.buy_item("Apple", 3)
cart1.buy_item("Banana", 2)
cart1.remove_item("Apple", 1)
print(cart1)
print()

"""
OBJECT 2 TEST CODE:
"""
# Test __init__ method with cart 2:
# Test __str__ method with cart 2:
# Test buy_item method with cart 2:
# Test remove_item method with cart 2:
cart2 = Cart()
cart2.buy_item("Orange", 4)
cart2.buy_item("Banana", 1)
cart2.remove_item("Orange", 2)
print(cart2)
print()

"""
OBJECT 3 TEST CODE:
"""
# Test __add__ method overload with two objects, cart1 and cart 2
# Test remove_item method with new object, combined_cart
combined_cart = cart1 + cart2
combined_cart.remove_item("Apple", 1)
print(combined_cart)
print()