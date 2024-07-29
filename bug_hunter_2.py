# Bug Hunter 2
# The bug police has heard of your remarkable skills asa Python programmer.
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

def is_even(number):
    if number % 2 == 0:  # number % 2 == 1 in the initial code means that there is a remainder of 1 when number is divided by 2.
        return True      # changed to == 0 because even number should have no remainder when divided by 2
    else: 
        return False

print(is_even(4))