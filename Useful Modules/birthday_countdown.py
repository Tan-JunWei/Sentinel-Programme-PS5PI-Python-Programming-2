import datetime

birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

current_date = datetime.datetime.now()

next_birthday = datetime.datetime(current_date.year, birth_date.month, birth_date.day)

if next_birthday < current_date:
    next_birthday = next_birthday.replace(year=current_date.year + 1)

days_left = (next_birthday - current_date).days

print(f"Today's date: {current_date}")
print(f"Next birthday: {next_birthday}")
print(f"Days left until your birthday: {days_left}")

# Helpful source: https://www.programiz.com/python-programming/datetime/strptime
# from datetime import datetime

# date_string = "21 June, 2018"

# print("date_string =", date_string)
# print("type of date_string =", type(date_string))

# date_object = datetime.strptime(date_string, "%d %B, %Y")

# print("date_object =", date_object)
# print("type of date_object =", type(date_object))