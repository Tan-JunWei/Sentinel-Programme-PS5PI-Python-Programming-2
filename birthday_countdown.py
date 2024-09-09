import datetime

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

current_date = datetime.datetime.now()
days_left = birth_date - current_date
print(f"Days left for your birthday: {days_left.days}")


# Helpful source: https://www.programiz.com/python-programming/datetime/strptime
# from datetime import datetime

# date_string = "21 June, 2018"

# print("date_string =", date_string)
# print("type of date_string =", type(date_string))

# date_object = datetime.strptime(date_string, "%d %B, %Y")

# print("date_object =", date_object)
# print("type of date_object =", type(date_object))