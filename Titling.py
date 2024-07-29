# Description
# For this exercise, do not use list comprehensions. Rather, use magic functions.

# We have users that sent us a list of countries. The problem is they don’t adhere to conventions, so the case is sometimes inconsistent. Look what this user has sent us:

# countries = ['ISRAEL', 'france', 'engLand', 'sinGAPore']
# We need to have a function called titling that returns a corrected list – where every country’s name begins with an uppercase letter, and the remaining letters are lowercase, for instance:

# >>> titling(countries)
# ['Israel', 'France', 'England', 'Singapore']
# Steps
# Implement the function titling(user_list) with the map function.
# Implement the main function to test out different inputs.

countries = ['ISRAEL', 'france', 'engLand', 'sinGAPore']

def titling(user_list):
    titled = print(list(map(lambda word : word.capitalize(), user_list)))

titling(countries)