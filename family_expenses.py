# Objectives
# Develop a Python application that calculates and reports the Johnson family's monthly finances.
# Practice reading from and writing to files, handling data, and producing output based on real-world requirements.
# Software Requirements
# Data Sources
# Your application will need to process information from two files:

# bank.txt - Contains the monthly expenses and income for each family member. Format: Each line includes a family member's name followed by their financial transactions, separated by commas. Incomes are positive numbers, while expenses are negative.

# hours.txt - Contains the number of work hours for the parents and the activity hours for the children each month. Format: Each line includes a family member's name followed by the relevant hours, separated by commas.

# Family Report
# The application should generate a report with the following details:

# For each family member:

# The total amount spent this month.
# The total income this month.
# The ending balance for the month (income minus expenses).
# Overall family details:

# The total work hours of the parents.
# The total activity hours of the children.
# Tasks
# Read and Process Data: Implement functionality to read data from the bank.txt and hours.txt files, parsing the information for further processing.

# Calculate Finances: For each family member, calculate the total expenses, total income, and ending balance. Also, compute the total work and activity hours as specified.

# Generate Report: Output a comprehensive report to the console, detailing the financial summary for each family member and the family's overall work and activity hours.

# Tips
# Ensure your code is modular, making use of functions or classes to organize the logic.
# Consider enhancing the user experience by formatting the output for easy reading.
# Make sure your code is well-written and PEP8 compliant.
 
member_info = {}
hours_info = {}

with open("bank.txt","r") as file:
    for line in file:
        member_info[line.strip().split(",")[0]] = [int(num) for num in line.strip().split(",")[1:]]

with open("hours.txt","r") as data:
    for line in data:
        hours_info[line.strip().split(",")[0]] = [int(num) for num in line.strip().split(",")[1:]]

def total_amount_spent(member_info):
    '''
    Calculate the total amount spend by each family member this month by adding up the negative values (expenses)
    ARGS:
    member_info: dictionary that includes lists which contain integer values of incomes and expenses of each family member
    
    RETURN:
    member_amount_spent: total amount spent this month
    '''
    member_amount_spent = {}  

    for key,list in member_info.items():
        expenses = 0
        for value in list:
            if value < 0:  # only account for expenses
                expenses += abs(value)
        member_amount_spent[key] = expenses

    return member_amount_spent

def total_income(member_info):
    '''
    Calculate the total income for each family member this month by adding up the positive values 
    ARGS:
    member_info: dictionary that includes lists which contain integer values of incomes and expenses of each family member
    
    RETURN:
    total_income: total income this month
    '''
    total_income = {}  

    for key,list in member_info.items():
        income = 0
        for value in list:
            if value > 0:  # only account for expenses
                income += abs(value)
        total_income[key] = income

    return total_income

def ending_balance():
    '''
    calculate the ending balance (income minus expenses) for each family member and store them in a dictionary

    RETURN:
    ending_balances: ending balance for the month
    '''
    total_incomes = total_income(member_info)
    total_expenses = total_amount_spent(member_info)
    
    ending_balances = {}

    for key in total_incomes.keys():
        ending_balance = total_incomes[key] - total_expenses[key]
        ending_balances[key] = ending_balance

    return ending_balances

def family_details(hours_info):
    '''
    calculate the total work/ activity hours of each family member
    ARGS: 
    hours_info: dictionary that includes a list containing number of hours of work/activity for each family member

    RETURN:
    total work/ activity hours of each family member
    '''
    member_hours = {}

    for key, value in hours_info.items():
        member_hours[key] = sum(value)
    
    return member_hours

total_amount_spent(member_info)
total_income(member_info)
ending_balance()
family_details(hours_info)

for key in member_info.keys():
    print(f"Financial summary for {key}:")
    print(f"Total amount spend this month: ${total_amount_spent(member_info)[key]:.2f}")
    print(f"Total income this month: ${total_income(member_info)[key]:.2f}")
    print(f"Ending balance for the month($): {ending_balance()[key]:.2f}")
    print(f"Total work/activity hours for {key}: {family_details(hours_info)[key]} hours\n")