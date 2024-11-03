# Bug Hunter 1
# The bug police has heard of your remarkable skills as a Python programmer.
# They have recruited you as a bug hunter to help themfi nd and fi x bugs in their code.
# Task
# Find the bug in the following code:
# Guidelines
# Use the strategies learned in Debugging lesson:
# Reading the error
# Debugging with print statements
# Rubber duck (explain your problem to someone or something)
# Debugging with
# pdb
# Submission
# Fixed code, with the fi xed line explained with a comment.

def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2  # radius was spelt wrongly as "raidus", causing a name error to be raised
    return area

print(calculate_area(5))