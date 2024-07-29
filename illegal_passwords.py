# Instructions
# Define a Custom Exception:

# Create a custom exception class named WeakPasswordError that inherits from Exception.
# Create a str method that shows a message - "Password is too weak."
# Create the Validation Function:

# Write a function validate_password(username, password) that checks the provided password against the weak password criteria:
# The password should not be "password" or "1234".
# The password should not be the same as the username.
# If the password meets any of the weak criteria, raise WeakPasswordError.
# Implement the Main Program:

# Prompt the user for their username and password.
# Use a try-except block to catch WeakPasswordError.
# If WeakPasswordError is caught, prompt the user to enter a stronger password


class WeakPasswordError(Exception):
    def __str__(self):
        return "Password is too weak."
    
def validate_password(username, password):
    if password == username or password == "password" or password == "1234":
        raise WeakPasswordError()

def main():
    username = input("Enter username: ")
    while True:
        password = input("Enter password: ")
        try: 
            validate_password(username,password)
            break
        except WeakPasswordError as e:
            print(e)
            print("Enter stronger password.")
    
    print("Password accepted.")

main()