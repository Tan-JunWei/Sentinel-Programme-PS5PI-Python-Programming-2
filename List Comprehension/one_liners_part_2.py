# One Liners - Part 2
# Introduction
# The king liked your one-liners so much, that he'd like you to have a go at another set of those.

# Tasks
# Task 1: Uppercase Words
# Given a list of words, use list comprehension to create a new list containing the uppercase version of each word.

# words = ["hello", "world", "python", "programming"]
# # Your list comprehension here
# Task 2: Word Lengths
# Given a list of words, use list comprehension to create a new list containing the lengths of each word.

# words = ["list", "comprehensions", "are", "powerful"]
# # Your list comprehension here
# Task 3: Exclude Vowels
# Given a string, use list comprehension to create a string that excludes all vowels from the original string. Consider 'a', 'e', 'i', 'o', 'u' as vowels.

# sample_string = "Look at those flying geese!"
# # Your list comprehension here
# Task 4: Find Palindromes
# Given a list of words, use list comprehension to find all words that are palindromes. A palindrome is a word that reads the same backward as forward.

# words = ["radar", "python", "level", "world", "madam"]
# # Your list comprehension here
# Task 5: Gimme Some Py
# Given a list of strings, use list comprehension to create a new list containing only the strings that contain the substring "py" or "Py".

# strings = ["python", "typography", "hyperloop", "Pythagoras", "apple"]
# # Your list comprehension here

# Task 1: Uppercase Words
words = ["hello", "world", "python", "programming"]
uppercase_words = [word.upper() for word in words]

# Task 2: Word Lengths
words = ["list", "comprehensions", "are", "powerful"]
word_lengths = [len(word) for word in words]

# Task 3: Exclude Vowels
sample_string = "Look at those flying geese!"
no_vowels = [char for char in sample_string if char.lower() not in ["a","e","i","o","u"]]

# Task 4: Find Palindromes
words = ["radar", "python", "level", "world", "madam"]
palindromes = [word for word in words if word == word[::-1]]

# Task 5: Gimme Some Py
strings = ["python", "typography", "hyperloop", "Pythagoras", "apple"]
contain_py = [string for string in strings if "py" in string or "Py" in string]


print(uppercase_words)
print(word_lengths)
print(no_vowels)
print(palindromes)
print(contain_py)