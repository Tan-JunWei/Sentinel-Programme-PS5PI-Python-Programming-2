# 1. Initialize Account
# Attributes:
# account_number: A unique identifier for the account (you can use a simple counter to generate unique account numbers).
# balance: Represents the current balance in the account (start with a default balance of $0).
# pin: A PIN number to secure the account (set by the user during account creation).
# 2. Deposit Money
# Method: deposit(amount)
# Allows the user to deposit money into their account, adding to the balance.
# 3. Withdraw Money
# Method: withdraw(amount, pin)
# Allows the user to withdraw money from their account if the PIN is correct and the balance is sufficient.
# 4. Check Balance
# Method: check_balance(pin)
# Displays the current balance if the PIN is correct.
# 5. Bank Account Manager
# Create a separate class called BankAccountManager that manages multiple bank accounts.
# Attributes:
# accounts: A dictionary to store the bank accounts, with the account number as the key and the BankAccount object as the value.
# Methods:
# create_account(pin): Creates a new BankAccount object with a unique account number and the provided PIN, then adds it to the accounts dictionary 
# and returns the new account number.
# get_account(account_number): Retrieves a BankAccount object from the accounts dictionary based on the provided account number.
# Tasks
# Implement the BankAccount class with the specified attributes and methods.
# Implement the BankAccountManager class to manage multiple bank accounts.
# Test your classes by creating multiple bank accounts, depositing and withdrawing money, and checking balances.
# Ensure your methods handle incorrect PIN inputs and insufficient balances gracefully, providing appropriate messages.

class BankAccount:
    def __init__(self, account_number, balance=0, pin=None):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if pin == self.pin and self.balance >= amount:
            self.balance -= amount
            return True
        elif self.balance < amount:
            return "Insufficient funds. Withdrawal canceled."
        elif pin != self.pin:
            return "Invalid PIN. Withdrawal canceled."

    def check_balance(self,pin):
        if pin == self.pin:
            return self.balance
        
class BankAccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, pin):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, pin=pin)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
manager = BankAccountManager()

account1 = manager.create_account("1234")
account2 = manager.create_account("5678")

manager.get_account(account1).deposit(1000)
manager.get_account(account2).deposit(500)

manager.get_account(account1).check_balance("1234")
manager.get_account(account2).check_balance("5678")

# Output: Current balance: $1000
print(f"Current balance: ${manager.get_account(account1).check_balance("1234")}")

# Output: Current balance: $1000
print(f"Current balance: ${manager.get_account(account2).check_balance("5678")}")

manager.get_account(account1).withdraw(200, "1234")
manager.get_account(account1).check_balance("1234")

# Output: Current balance: $800
print(f"Current balance: ${manager.get_account(account1).check_balance("1234")}")

# Attempt to withdraw money with an incorrect PIN
manager.get_account(account2).withdraw(100, "1111")  
print(manager.get_account(account2).withdraw(100, "1111"))# Output: Invalid PIN. Withdrawal canceled.

# Attempt to withdraw more money than the available balance
manager.get_account(account2).withdraw(1000, "5678")  
print(manager.get_account(account2).withdraw(1000, "5678")) # Output: Insufficient funds. Withdrawal canceled.