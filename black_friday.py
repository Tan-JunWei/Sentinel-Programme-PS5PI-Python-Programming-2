# Your task
# Write a Python script that:

# Defines a list of tuples for various products. Each tuple should contain the product's name and its original price.
# Use the following list: products = [("Laptop", 1200), ("Phone", 700), ("Camera", 450), ("Headphones", 150)].
# Uses list comprehension to apply the following discount policy:
# If the original price is greater than $500, apply a 20% discount.
# If the original price is $500 or less, apply a 10% discount.
# Ensures the new prices are rounded to 2 decimal places for readability.
# Use the builtin round function for this purpose.
# Example:
# >>> price = round(52.123482)
# >>> print(price)
# 52.12
# Print the original list and the new list with applied discounts.
# Example Output
# Original Prices:
# [('Laptop', 1200), ('Phone', 700), ('Camera', 450), ('Headphones', 150)]

# Discounted Prices:
# [('Laptop', 960.0), ('Phone', 560.0), ('Camera', 405.0), ('Headphones', 135.0)]

# Requirements
# Use a single list comprehension to generate the new list of discounted products.
# Use conditional logic (if-else) within the comprehension to support different discount rates.

products = [("Laptop", 1200), ("Phone", 700), ("Camera", 450), ("Headphones", 150)]
discounted = [(product[0], 80 / 100 * product[1]) if product[1] > 500 else (product[0], 90 /100 * product[1]) for product in products]

print("Original Price:")
print(products)

print("Discounted Price:")
print(discounted)