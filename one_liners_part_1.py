# One Liners - Part 1
# Introduction
# Our beloved King Kahuka decided that things should be more efficient in his kingdom.

# From now on, each task should be performed using only one line of code.

# Your tasks
# Task 1: Filter Even Numbers
# Given a list of integers, use list comprehension to create a new list containing only the even numbers.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Write your one-line here
# Task 2: Square Numbers
# Generate a list of squares of the integers from 1 to 10 using list comprehension.

# Task 3: Celsius to Fahrenheit
# Convert a list of temperatures from Celsius to Fahrenheit. Use the formula F = C * 9/5 + 32.

# Task 4: Extract Names Starting with a Specific Letter
# Given a list of names, use list comprehension to create a new list containing only the names starting with S.

# names = ["Sarah", "John", "Charles", "Sebastian", "Sophie"]
# # Write your one-line here
# Task 5: Filter Negative Numbers and Square the Rest
# From a given list of integers, use list comprehension to eliminate any negative numbers and square the remaining numbers.

# original_list = [1, -2, 3, 4, -5, 6]
# # Write your one-line here
# Task 6: Create a List of Tuples
# Given a list of integers, use list comprehension to create a new list of tuples (x, y), where x is the original integer, and y is the square of the integer.

# numbers = [1, 2, 3, 4, 5]
# # Write your one-line here
# # The output should be [(1, 1), (2, 4), (3, 9), ...]
# Instructions
# For each task, write the corresponding list comprehension statement.
# Ensure your solutions follow Python's PEP 8 style guide for readability.
# Test your solutions to ensure they work as expected.

numbers = [1,2,3,4,5,6,7,8,9,10]

# Task 1: even numbers
even = [num for num in numbers if num % 2==0]  

 # Task 2: squared numbers
squared = [num ** 2 for num in numbers] 

temperature_in_celsius = [27,29,32]  # since no temperature list was provided

# Task 3: convert temp in celsius to fahrenheit using F = C * 9/5 + 32
fahrenheit = [temp * 9/5 + 32 for temp in temperature_in_celsius] 

names = ["Sarah", "John", "Charles", "Sebastian", "Sophie"]

# Task 4: names starting with S
names_starting_with_s = [name for name in names if name[0] == "S"]

original_list = [1, -2, 3, 4, -5, 6]

# Task 5: eliminate negative numbers and square remaining
no_negative_squared = [num ** 2 for num in original_list if num >= 0]

numbers = [1, 2, 3, 4, 5]

# Task 6: create a new list of tuples (x, y), where x is the original integer, and y is the square of the integer.
list_of_tuples = [(x,x**2) for x in numbers]

print(even)
print(squared)
print(fahrenheit)
print(names_starting_with_s)
print(no_negative_squared)
print(list_of_tuples)
