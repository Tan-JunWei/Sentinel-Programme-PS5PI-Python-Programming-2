# Your task
# Implement the create_event function that gets an event name and a date string and returns an Event object.
# Implement an Event class with attributes for the event's name, year, month, and day.
# Handle invalid inputs by raising and catching appropriate exceptions (see below).
# Date Format and Validation
# The input date string format is "dd/mm/yyyy".
# Validate the date to ensure it corresponds to a valid calendar date, considering the number of days in each month (excluding leap years).
# Months have the following number of days: January (31), February (28), March (31), April (30), May (31), June (30), July (31), August (31), September (30), October (31), November (30), December (31).
# Raise a ValueError for invalid dates (e.g., 30th of February).
# Exception Handling
# In the main function, continuously prompt the user for a date string until a valid one is entered.
# Use try-except blocks to catch ValueError exceptions, informing the user of the invalid input and prompting for a new input.
# Use the following template (fill your code where specified).

class Event:
    def __init__(self, name, day, month, year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year

def create_event(name, date_str):
    while True:
        try:
            day, month, year = map(int, date_str.split("/"))
            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError("Invalid date format or invalid date values.")
            break  # If valid: break out of the loop
        except ValueError:
            print("Invalid date format. Please enter the date in dd/mm/yyyy format.")
            date_str = input("Enter the event date (dd/mm/yyyy): ")

    return Event(name, day, month, year)

def main():
    event_name = input("Enter the event name: ")
    date_str = input("Enter the event date (dd/mm/yyyy): ")
    
    event = create_event(event_name, date_str)
    
    print(f"Event '{event.name}' created for {event.day}/{event.month}/{event.year}")

if __name__ == "__main__":
    main()
