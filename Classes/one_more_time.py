# In this exercise, you will create a Time class that represents a time in hours, minutes, and seconds.

# Your class will be super cool, because it will support time addition (time1 + time2).

# Background
# In Python, the + operator is used to add numbers or concatenate strings and lists.

# However, you can define the __add__ method in your custom class to specify how the + operator should work with instances of that class.

# When the + operator is used on instances of your class, Python automatically calls the __add__ method to perform the addition.

# Class Description
# The Time class should have the following attributes and methods:

# Attributes:

# hours (private): An integer representing the hours component of the time.
# Value between 00 to 99.
# minutes (private): An integer representing the minutes component of the time.
# Value between 00 to 59.
# seconds (private): An integer representing the seconds component of the time.
# Value between 00 to 59.
# Methods:

# __init__(self, hours, minutes, seconds): Initializes a new Time instance with the specified hours, minutes, and seconds.
# __str__(self): Returns a string representation of the time in the format "HH:MM:SS".
# It is automatically called by Python when trying to print your instance.
# __add__(self, other): It expects another Time instance as the other parameter and returns a new Time instance representing the 
# sum of the two times.
# It is automatically called by Python on time1 when performing time1 + time2.
# In this case, time1 will be self and time2 will be other.
# If the hour value becomes greater than 99, keep the remainder of 99.
# For example, 101 would become 02.
# Example Usage
# # Create Time instances
# time1 = Time(2, 30, 45)
# time2 = Time(1, 45, 30)

# # Add times using the overridden + operator
# result = time1 + time2

# # Print the times and the result
# print(time1)   # Output: 02:30:45
# print(time2)   # Output: 01:45:30
# print(result)  # Output: 04:16:15


class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
    
    def __add__(self, other):
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        total_seconds += other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours % 100, minutes, seconds)

time1 = Time(2, 30, 45)
time2 = Time(1, 45, 30)

result = time1 + time2
print(time1)
print(time2)
print(result)