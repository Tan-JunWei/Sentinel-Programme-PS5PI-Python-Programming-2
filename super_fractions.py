# Task
# Extend the Fraction class from the previous exercise to support subtraction, multiplication, and division operations. The class should have the following additional methods:

# __sub__(self, other): Override the - operator to subtract two fractions.
# __mul__(self, other): Override the * operator to multiply two fractions.
# __truediv__(self, other): Override the / operator to divide two fractions.
# Subtraction, Multiplication, and Division of Fractions
# To subtract fractions:

# Find the Least Common Multiple (LCM) of the denominators.
# Convert each fraction to have the LCM as the denominator.
# Subtract the numerators of the converted fractions.
# Simplify the resulting fraction if possible.
# To multiply fractions:

# Multiply the numerators of the fractions.
# Multiply the denominators of the fractions.
# Simplify the resulting fraction if possible.
# To divide fractions:

# Multiply the first fraction by the reciprocal of the second fraction.
# Simplify the resulting fraction if possible.
# Example
# fraction1 = Fraction(1, 3)
# fraction2 = Fraction(2, 5)

# result_sub = fraction1 - fraction2
# print(result_sub)  # Output: -1/15

# result_mul = fraction1 * fraction2
# print(result_mul)  # Output: 2/15

# result_div = fraction1 / fraction2
# print(result_div)  # Output: 5/6
# Tips
# Use the __add__ method from the previous exercise as a reference for implementing the other operations.
# Remember to simplify the resulting fractions after each operation.

import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        new_numerator = (self.numerator * (lcm // self.denominator)) + (other.numerator * (lcm // other.denominator))
        return Fraction(new_numerator, lcm).simplify()
    
    def __sub__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        new_numerator = (self.numerator * (lcm // self.denominator)) - (other.numerator * (lcm // other.denominator))
        return Fraction(new_numerator, lcm).simplify()
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator).simplify()
    
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator).simplify()
    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        return self

frac1 = Fraction(1, 3)
frac2 = Fraction(2, 5)

print(frac1 + frac2)
print(frac1 - frac2)  
print(frac1 * frac2)  
print(frac1 / frac2)  