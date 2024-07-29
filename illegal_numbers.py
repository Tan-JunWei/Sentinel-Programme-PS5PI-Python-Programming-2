# Task
# Write a Python script that performs the following:

# Prompt User for Input:

# Ask the user to input two numbers, numerator and denominator.
# Perform Division:

# Attempt to divide the numerator by the denominator and print the result.
# Handle Exceptions:

# Implement error handling to catch and respond to the following potential issues:
# Division by zero (ZeroDivisionError).
# Non-numeric input (ValueError).
# User Feedback:

# If an exception occurs, print an appropriate message to the user. For example:
# If the user attempts division by zero, print "Error: Cannot divide by zero."
# If the user enters a non-numeric value, print "Error: Please enter a valid number."
# Ensure Program Continuity:

# Regardless of whether an exception occurs, prompt the user to try again or exit the program gracefully.
# Example Output
# Enter the numerator: 10
# Enter the denominator: 2
# Result: 5.0

# Try again? (y/[n]): y
# Enter the numerator: 10
# Enter the denominator: 0
# Cannot divide by zero!

# Try again? (y/[n]): y
# Enter the numerator: abc
# Please enter a valid number.

# Try again? (y/[n]): n
# Guidelines
# Use try and except blocks to handle exceptions.
# Utilize a loop to allow the user multiple attempts until they choose to exit.
# Ensure your code is clean and well-commented to explain your logic.

def division_of_numbers():
    try: 
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            print(f"Result: {numerator/denominator}")
    except ValueError:
        print("Error: Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

while True:
    division_of_numbers()
    option = input("Try again? (y/n): ")
    if option.lower() == 'y':
        continue
    elif option.lower() =='n':
        break



