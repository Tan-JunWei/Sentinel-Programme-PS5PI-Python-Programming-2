# Description
# For this exercise, do not use list comprehensions. Rather, use magic functions. Specifically the reduce function.

# We want to get a list of words, and add them together with an arrow ("->") Between each word:

# Input: ["Hello", "My", "Name", "Is", "Slim Shady"]
# Output: "Hello->My->Name->Is->Slim Shady"
# Steps
# Implement the function reduce_words(user_list) with the reduce function.
# Implement the main function to test out different inputs.

from functools import reduce

word_list = ["Hello", "My", "Name", "Is", "Slim Shady"]

def reduce_words(accumulator, current_word):
    return f"{accumulator}->{current_word}"

result = reduce(reduce_words, word_list)
print(result)

