# Your task
# Your program should:

# Ask for the desired number of servings

# Prompt the user to input the number of servings they intend to make
# Adjust the Recipe:

# Calculate the new quantities for each ingredient, based on the new number of servings.
# Print the new quantities for each ingredient.
# Example Recipe
# This is a dictionary representing the original recipe ingredients for 2 servings:

# ingredients = {
#     "flour (cups)": 2,
#     "sugar (cups)": 1,
#     "eggs": 2,
#     "milk (cups)": 1,
#     "butter (cups)": 0.5,
# }
# Use it in your script as a basis for your calculations.

# Example output
# Desired number of servings: 8

# Original Recipe Ingredients:
# flour (cups): 2
# sugar (cups): 1
# eggs: 2
# milk (cups): 1
# butter (cups): 0.5

# New recipe quantities:
# flour (cups): 8.00
# sugar (cups): 4.00
# eggs: 8.00
# milk (cups): 4.00
# butter (cups): 2.00
# Guidelines
# Make sure that your code is well-organized and readable, using the PEP8 conventions.
# Ensure your script is well-commented to explain the logic behind your calculations.

servings = int(input("Desired number of servings: "))

ingredients = {
    "flour (cups)": 2,
    "sugar (cups)": 1,
    "eggs": 2,
    "milk (cups)": 1,
    "butter (cups)": 0.5,
}

adjusted = {key:value * (servings/2) for key, value in ingredients.items()}

print("Original Recipe Ingredients: ")
print(ingredients)
print("Adjusted Recipe Quantities:")
print(adjusted)