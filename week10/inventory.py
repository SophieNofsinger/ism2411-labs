# inventory.property
# # Author: Sophia Nofsinger
# # Module 10 Lab: Inventory List Manager

# Reflection Questions
# 1) What is the most surprising thing about how lists work in Python compared to what you expected coming in?
# a) The most surprising thing about Python lists compared to what I was expecting is how easy it is to organize, access, and change multiple pieces of information.
# 2) Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
# a) A python list would be helpful at my job at Bath & Body Works for keeping track of inventory. Instead of manually organizing products in Excel, I could track everything, check stock, and quickly update inventory when items are sold or restocked.

# Exercise 1: build a list
print("--- Exercise 1: Build a List ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")

print(inventory[0]) # grabs the first item
print(inventory[-1]) # grabs the last item

middle = len(inventory)// 2
print(inventory[middle]) # grabs the middle item

# Exercise 3: Slicing

print("--- Exercise 3: Slicing ---")

print(inventory[:3]) # grabs the first three items
print(inventory[-2:]) #grabs the last two items
print(inventory[::2])

# Exercise 4: Modify

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of the list
inventory.append("tape") # adds an item to the end of the list
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

# Exercise 5: Tuple Comparison

print("--- Exercise 5: Tuple Comparison")

coords = (40.7128, -74.0060) # New York City coordinantes

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinantes from being changed by accident.")

# Exercise 6: Average of a list of sales

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sales: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"worst sale (loop): {worst}")

# Exercise 7: Accumulator pattern

print("--- Exercise 7: Accumulator Pattern")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount. 2 rounds to 2 decimal places.

print(prices)
print(discounted)

# Exercise 8: Filter above threshold

print("--- Exercise 8: Filter ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # an empty list

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
