
# Introduction
# In this exercise, you will create a Fraction class that represents a fraction.

# Your class will be extra cool, because it will support fractions addition (fraction1 + faction2).

# Background
# In Python, the + operator is used to add numbers or concatenate strings and lists.

# However, you can define the __add__ method in your custom class to specify how the + operator should work with instances of that class.

# When the + operator is used on instances of your class, Python automatically calls the __add__ method to perform the addition.

# Class Description
# The Fraction class should have the following attributes and methods:

# Attributes:

# numerator (integer)
# denominator (integer)
# Methods:

# __init__(self, numerator, denominator): Initialize the fraction.
# __str__(self): Return the fraction as a string (e.g., "1/3").
# __add__(self, other): Overrides the + operator to perform fraction addition. It takes another Fraction instance as the other parameter and returns a new Fraction instance representing the sum of the two fractions.
# simplify(self): Simplify the fraction to its lowest terms.
# Example Usage
# fraction1 = Fraction(1, 3)
# fraction2 = Fraction(2, 5)
# result = fraction1 + fraction2
# print(result)  # Output: 11/15
# How to Add Fractions
# To add two fractions:

# Find the Least Common Multiple (LCM) of the denominators.
# Convert each fraction to have the LCM as the denominator.
# Add the numerators of the converted fractions.
# Simplify the resulting fraction if possible.
# Tips
# Use math.lcm() or a custom function to calculate the LCM.
# Use math.gcd() to find the Greatest Common Divisor (GCD) for simplification.

import math

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self,other):
        lcm = math.lcm(self.denominator, other.denominator)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(new_numerator,lcm)
    
    def simplify(self):
        gcd = math.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

fraction1 = Fraction(1, 3)
fraction2 = Fraction(2, 5)

result = fraction1 + fraction2

print(result)