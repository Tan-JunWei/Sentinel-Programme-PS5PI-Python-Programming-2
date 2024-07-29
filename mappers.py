# Description
# So far we've been writing Python code without any magic functions, now we want to see how we can solve complex stuff with magic functions!

# Steps
# Implement a one liner with the map function to generate a list of squares from a given number list.
# Input: [1, 2, 3]
# Output: [1, 4, 9]
# Implement a one liner with the map function that given a number list, will return a list with every number turned into a string
# Input: [8, 24, 4]
# Output: ["8", "24", "4"]
# Implement a one liner with the map function that given a list of strings, will remove all of the occurences of the letter "t" from all of the strings
# Input: ["hello", "tom", "sentinal", "robert"]
# Output: ["hello", "om", "seninal", "rober"]

# Step 1
print(list(map(lambda num: num ** 2, [1,2,3])))

# Step 2
print(list(map(lambda num: str(num),[8,24,4])))

# Step 3
print(list(map(lambda word : word.replace("t",""), ["hello", "tom", "sentinal", "robert"])))

