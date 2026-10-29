# AI DISCLOSURE: I used AI to assist me in fixing each trace back.

# Self-Assesment Questions
# 1) In Exercise 5 (Debug First, Then Ask), what was the first bug you spotted? Did you find it from the traceback, from a print() statement, from explaining the code out loud to the duck, or only after asking AI? What does that tell you about your current debugging instincts?
# a) The first bug that I spotted in Exercise 5 was the missing : in line 11. I noticed the bug originally without checking the traceback because I knew that a : was needed to include the following instructions in the loop. The traceback confirmed my suspicions and I then explained to a duck why the error occured. I struggled a lot more with the other bugs, but at least with this one I feel confident about my debugging instincts.
# 2) Without looking at your code, explain in plain English what apply_discount(price, tier) does, what its inputs are, and what it returns. Could a colleague use it without reading the body?
# a) apply_discount(price, tier) takes a price and discount tier as inputs and returns the price after calculating the discount. Gold gives you 15%, silver is 10%, and bronze is 5%. A colleague could read it without having to read the body.
# 3) If you used AI on any part of today's lab, write the disclosure comment you would add to the top of your file. Then reflect: did the AI use build your understanding, or did it shortcut it?
# a) I think that the AI I used helped me to better understand why my code works rather than just having a surface level of knowing that it does work.

# -- Exercise 1: calculate_tax --

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at %%: ${calculate_tax(350, 0.05):.2f}")

# -- Exercise 2: apply_discount --

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# -- Exercise 3: Compose them --

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# -- Exercise 4: Loop + function --

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# -- Exercise 6: Scope experiment --

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # 100
print(double_it()) # 1998
print(x)           # 100

# Scope determines where a variable can be used. The x inside the function is local to the function, so it does not change the global x.