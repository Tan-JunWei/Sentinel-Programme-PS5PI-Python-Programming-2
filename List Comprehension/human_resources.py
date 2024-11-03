# Task
# Given the following 3 dictionaries, create a new dictionary that maps employee names to their respective departments.

# employee_names: Maps employee IDs (as keys) to employee names (as values).
# employee_departments: Maps employee IDs (as keys) to department IDs (as values).
# department_names: Maps department IDs (as keys) to department names (as values).

# Example Data
# employee_names = {
#     1: 'Alice Smith',
#     2: 'Bob Jones',
#     3: 'Charlie Brown',
#     4: 'Hilary Jobs'
# }

# employee_departments = {
#     1: 101,
#     2: 101,
#     3: 102,
#     4: 103,
# }

# employee_departments = {
#     101: 'Finance',
#     102: 'Marketing',
#     103: 'Human Resources'
# }

# Expected Output
# Alice Smith: Finance
# Bob Jones: Finance
# Charlie Brown: Marketing
# Hilary Jobs: Human Resources

employee_names = {
    1: 'Alice Smith',
    2: 'Bob Jones',
    3: 'Charlie Brown',
    4: 'Hilary Jobs'
}

employee_department = {
    1: 101,
    2: 101,
    3: 102,
    4: 103,
}

employee_departments = {
    101: 'Finance',
    102: 'Marketing',
    103: 'Human Resources'
}

employee_and_dept = {value: employee_departments[employee_department[key]] for key, value in employee_names.items()}
print(employee_and_dept)