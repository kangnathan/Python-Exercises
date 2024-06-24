print("WELCOME TO EVERYTHING STORE")

item = input("What would you like to buy? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many {item}s would you like to buy? "))

print(f"Added {quantity} {item} to your cart.")

print(f"You have a subtotal of PHP{price * quantity}")





