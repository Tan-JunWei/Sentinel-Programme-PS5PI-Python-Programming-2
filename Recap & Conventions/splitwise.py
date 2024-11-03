# Your task
# Write a Python script that:

# Defines a list of expenses: Each expense is represented as a dictionary that includes the amount paid and the name of the person who paid it (see example).

# Calculates total expenses and individual shares: Determine the total amount spent, how much each person has paid, and how much each person owes / is owed.

# Prints a summary of transactions: Print the transactions needed for everyone to settle their debts, showing who owes whom and how much.

# Example Input
# Your program should be able to process input like the following:

# expenses = [
#     {"amount": 120, "paid_by": "Alice"},
#     {"amount": 140, "paid_by": "Bob"},
#     {"amount": 190, "paid_by": "Charlie"},
#     {"amount": 90, "paid_by": "Alice"},
# ]
# Use this input to test your code.

# Example output
# Total Expense: $540.00
# Each person's share: $180.00

# Transactions to settle up:
# Bob owes Alice: $30.00
# Bob owes Charlie: $10.00
# Guidelines
# Before starting coding, think about how to solve the problem. Write the calculations on paper, and only then translate them to code.

# expenses = [
#     {"amount": 120, "paid_by": "Alice"},
#     {"amount": 140, "paid_by": "Bob"},
#     {"amount": 190, "paid_by": "Charlie"},
#     {"amount": 90, "paid_by": "Alice"},
# ]

expenses = [
    {"amount": 300, "paid_by": "Alice"},
    {"amount": 140, "paid_by": "Bob"},
    {"amount": 10, "paid_by": "Charlie"},
    {"amount": 90, "paid_by": "Alice"},
]

total = 0
paid = {}
settle_transactions = {}

for dictionary in expenses:
    total += dictionary["amount"]

    if dictionary["paid_by"] in paid.keys():
        paid[dictionary["paid_by"]] += dictionary["amount"]
    else: 
        paid[dictionary["paid_by"]] = dictionary["amount"]

individual_share = total/len(paid)

for key,value in paid.items():
    if value < individual_share:
        name = key
    else:
        settle_transactions[key] = value - individual_share

print(f"Total Expense: ${total:.2f}")
print(f"Each person's share: ${individual_share:.2f}")
print("\nTransactions to settle up:")

for key, value in settle_transactions.items():
    print(f"{name} owes {key}: ${value:.2f}")