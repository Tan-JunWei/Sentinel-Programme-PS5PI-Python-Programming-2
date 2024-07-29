# Task
# Write a Python script that performs the following operations:

# Prompt User for File Path:

# Ask the user to input the path to the text file containing the social media posts.
# Extract Hashtags from Each Post:

# Open and read the file line by line, extracting hashtags from each post.
# Count the Frequency of Each Hashtag:

# Use a dictionary to track how many times each hashtag appears.
# Identify and Output the Top 5 Most Popular Hashtags:

# Sort the hashtags by their frequency in descending order.
# Print the top 5 hashtags and their counts.
# Input text file format
# Your program should expect a text file containing social media posts, one per line.

# Each post may include hashtags, which are words preceded by the # symbol. For example:

# Today was an amazing day! #life #amazing
# Just finished reading a great book on #Python and I highly recommend it! #programming #coding
# I love #Python ! It's such a versatile language. #coding #programming
# Exploring the great outdoors. #nature #life
# Example run output
# Top 5 hashtags and their counts:
# #coding: 3
# #python: 3
# #morningrituals: 2
# #health: 2
# #learning: 2
# Guidelines
# Make sure that your code is well-organized and readable, using the PEP 8 conventions.
# Normalize the hashtags to lowercase before counting to avoid duplicate counts due to case differences. For example: #Python and #python count as the same hashtag.
# Comment your code to explain your logic and decisions.

# social_media_posts.txt
file_path = input("Enter file path: ")
hashtags = []
hashtag_dict = {}

with open(file_path,"r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if "#" in word:
                hashtags.append(word.lower())

for hashtag in hashtags:
    hashtag_dict[hashtag] = hashtags.count(hashtag)

sorted_hashtags = dict(sorted(hashtag_dict.items(), key = lambda item : item[1], reverse = True))

print("Top 5 hashtags and their counts:")
for i in range(5):
    print(f"{list(sorted_hashtags.items())[i][0]}: {list(sorted_hashtags.items())[i][1]}")
