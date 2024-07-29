import sys
from math import pow
import os

def calc_sum(x,y):
    '''Calculate sum of two numbers, x and y'''
    return x + y

def calc_product(x,y):
    '''Calculate the product of two numbers, x and y'''
    return x * y 

def calc_difference(x,y):
    '''Calculate the difference of two numbers, x and y'''
    return x - y  # calculate difference

def calc_quotient(x,y):
    '''Calculate the quotient of two numbers, checking for division by zero'''
    if y == 0:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return x / y

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

total_sum = calc_sum(list_of_numbers[0],list_of_numbers[1])
print("Total Sum:",total_sum)

total_product = calc_product(list_of_numbers[2],list_of_numbers[3])
print("Total Product:",total_product)
    
total_difference=calc_difference(list_of_numbers[4],list_of_numbers[5])
print("Total Difference:", total_difference)

total_quotient=calc_quotient(list_of_numbers[6],list_of_numbers[7])
print("Total Quotient:",total_quotient)