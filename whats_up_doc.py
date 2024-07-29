# What's Up, Doc?
# Instructions
# Someone has stolen all of the function names, variables names and documentation!

# Understand what this code does, and restore the missing variable and function names, and the documentation.

# Provided Script

import random

def random_numbers(size, lower_bound, upper_bound):
    '''
    generate a list of random integers within a specified range
    ARGS:
    size: number of numbers
    lower_bound: minimum of numbers
    upper_bound: maximum of numbers

    return list of random integers
    '''
    result = []
    for _ in range(size):
        result.append(random.randint(lower_bound, upper_bound))
    return result

def even_numbers(numbers):
    '''
    filters out the even numbers from a list of random integers
    ARGS:
    numbers: list of random integers 
    
    return filtered list of even numbers
    '''
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def primes(numbers):
    '''
    filters out the prime numbers from a list of random integers
    ARGS:
    numbers: list of random integers 
    
    return filtered list of prime numbers
    '''
    mystery_list = []
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            mystery_list.append(num)
    return mystery_list

def sum(numbers):
    return sum(numbers)