# One Liners - Part 3
# Introduction
# The king has decided to raise the bar, and test your dict comprehension skills as well.

# Tasks
# Task 1: Word Frequency Counter
# Objective: Given a sentence, use dict comprehension to count the frequency of each word in the sentence. Ignore case sensitivity.

# Example:
# sentence = "Hello world World hello"
# # Your dict comprehension here
# Task 2: Invert a Dictionary
# Objective: Given a dictionary, use dict comprehension to invert its keys and values. Assume all values are unique and hashable.

# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # Your dict comprehension here
# Task 3: Square Numbers Mapping
# Objective: Generate a dictionary where the keys are numbers from 1 to 10 and the values are the squares of the keys.

# Example:
# # Your dict comprehension here
# Task 4: Filter Dictionary by Value
# Objective: Given a dictionary, use dict comprehension to create a new dictionary with key-value pairs for entries where the value is greater than a certain threshold.

# Example:
# my_dict = {'a': 10, 'b': 15, 'c': 5}
# threshold = 10
# # Your dict comprehension here
# Task 5: Create a Dictionary from Two Lists
# Objective: Given two lists of equal length, one representing keys and the other representing values, use dict comprehension to create a dictionary mapping keys to values.

# Example:
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# # Your dict comprehension here

# Task 1: Word Frequency Counter
sentence = "Hello world World hello"
word_dict = {word:len(word) for word in sentence.split()}

# Task 2: Invert a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted = {value:key for key, value in my_dict.items()}

# Task 3: Square Numbers Mapping
squares = {x:x**2 for x in range(1,11)}

# Task 4: Filter Dictionary by Value
my_dict = {'a': 10, 'b': 15, 'c': 5}
threshold = 10
filtered = {key:value for key,value in my_dict.items() if value > threshold}

# Task 5: Create a Dictionary from Two Lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {key:value for key, value in zip(keys,values)}

print(word_dict)
print(inverted)
print(squares)
print(filtered)
print(dictionary)