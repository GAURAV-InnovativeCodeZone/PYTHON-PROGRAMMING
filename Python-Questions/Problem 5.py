'''
Create a class named Order with attribute like items and price.
Implement a method to display the order details.
'''

class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def display_order_details(self):
        print("Order Details:")
        print(f"Items: {self.items}")
        print(f"Price: {self.price}")
    
    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        return self.price < other.price
# Example usage
order1 = Order(["Pizza", "Burger"], 25.99)
order1.display_order_details()
order2 = Order(["Pasta", "Salad"], 35.49)
order2.display_order_details()

print(f"Is order1 more expensive than order2 ?  {'Yes' if order1 > order2 else 'No'}")
