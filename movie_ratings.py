# Task
# Your program should perform the following tasks:

# Read Ratings: Read movie ratings from three separate text files, each containing ratings from one of the sources (IMDb, Rotten Tomatoes, Metacritic).

# Convert IMDb Ratings: Convert IMDb ratings from a scale of 1-10 to a scale of 1-100.

# Calculate Average Rating: For each movie, calculate the average rating based on the ratings from all three sources.

# Print Results: Display the average rating for each movie.

# Implementation Guidelines
# Use list comprehension or dict comprehension where it makes sense to simplify your code.
# Example Data
# IMDb Ratings (imdb_ratings.txt):

# The Shawshank Redemption: 9.3
# Inception: 8.8
# The Dark Knight: 9.0
# Rotten Tomatoes Ratings (rotten_tomatoes_ratings.txt):

# The Shawshank Redemption: 90
# Inception: 86
# The Dark Knight: 94
# Metacritic Ratings (metacritic_ratings.txt):

# The Shawshank Redemption: 80
# Inception: 74
# The Dark Knight: 82
# Example Output

# Average Ratings:
# The Shawshank Redemption: 87.67
# Inception: 82.67
# The Dark Knight: 88.67

with open("imdb_ratings.txt","r") as file:
    imdb = {}
    for line in file:  
        data = line.strip().split(":")
        imdb[data[0]] = float(data[1]) * 10

with open("rotten_tomatoes_ratings.txt","r") as file:
    rotten = {}
    for line in file:  
        data = line.strip().split(":")
        rotten[data[0]] = float(data[1])

with open("meta_critic_ratings.txt","r") as file:
    metacritic = {}
    for line in file:  
        data = line.strip().split(":")
        metacritic[data[0]] = float(data[1])

average = {key:round((imdb[key]+rotten[key]+metacritic[key]) / 3,2) for key in imdb.keys()}

# print(imdb)
# print(rotten)
# print(metacritic)
print(average)



