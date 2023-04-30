tax = 0.12
delivery = 250

Bookandprices = {    "Introduction to Python Programming": 499.00,    "Python Libraries Cookbook": 855.00,    "Data Science in Python": 645.00  }


Book_quantity = {}
for book, price in Bookandprices.items():
    quantity = int(input(f"How many {book}s would you like to buy? --> "))
    Book_quantity[book] = quantity

subtotal = 0
for book, quantity in Book_quantity.items():
    price = Bookandprices[book]
    subtotal += price * quantity
tax_amount = subtotal * tax

total_amount = subtotal + tax_amount + delivery

print("Total Invoice Amount with 12% GST and Rs.250 Delivery Charges: Rs.", total_amount)
