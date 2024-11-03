# Class Description
# The Hangman class represents the game logic and state. It should have the following methods:

# __init__(self, word_list, max_attempts): Initializes a new Hangman game with the specified word list and maximum 
# number of attempts.
# guess_letter(self, letter): Processes the player's guessed letter and updates the game state accordingly.
# is_game_over(self): Checks if the game is over (player has guessed the word or run out of attempts).
# get_masked_word(self): Returns the masked version of the chosen word, showing only the correctly guessed letters.
# get_attempts_left(self): Returns the remaining number of attempts the player has.
# Tasks
# Implement the Hangman class with the specified methods.
# Use private attributes (which are indicated by starting with double underscores __) to store the internal game state
# and logic. These attributes should only be accessed and modified within the class methods.
# For example: keep track of the attempts left by having a private attribute self.__attempts_left.
# In the __init__ method, randomly select a word from the provided word_list and initialize the game state accordingly.
# In the guess_letter method, check if the guessed letter is present in the chosen word and update the game state 
# accordingly.
# In the is_game_over method, determine if the game is over based on the player's guesses and remaining attempts.
# It should return True if the player has guessed the word or run out of attempts, and False otherwise.
# In the get_masked_word method, return the current state of the masked word, revealing only the correctly guessed letters.
# For example: if the player has guessed the letters "p" and "n" in the word "python", the masked word should be "p____n".
# In the get_attempts_left method, return the current number of attempts left for the player.
# Example Usage
# Create an instance of the Hangman class
# word_list = ["python", "programming", "cyber"]
# game = Hangman(word_list, max_attempts=6)

# # Play the game
# while not game.is_game_over():
#     print(game.get_masked_word())
#     print(f"Attempts left: {game.get_attempts_left()}")
#     letter = input("Enter a letter: ")
#     game.guess_letter(letter)

# # Print the game result
# if game.get_attempts_left() > 0:
#     print("Congratulations! You guessed the word correctly.")
# else:
#     print("Game over! You ran out of attempts.")

import random

class Hangman:
    def __init__(self, word_list, max_attempts):
        self.__word_list = word_list
        self.__max_attempts = max_attempts
        self.__chosen_word = random.choice(word_list)
        self.__masked_word = "_" * len(self.__chosen_word)
        self.__attempts_left = max_attempts
        self.__guessed_letters = set()
    
    def guess_letter(self, letter):
        if letter in self.__chosen_word:
            for i in range(len(self.__chosen_word)):
                if self.__chosen_word[i] == letter:
                    self.__masked_word = self.__masked_word[:i] + letter + self.__masked_word[i+1:]
        else:
            self.__attempts_left -= 1
        self.__guessed_letters.add(letter)

    def is_game_over(self):
        # either correctly guessed word or no attempts left
        return self.__masked_word == self.__chosen_word or self.__attempts_left == 0 

    def get_masked_word(self):
        return self.__masked_word
    
    def get_attempts_left(self):
        return self.__attempts_left
    
word_list = ["python", "programming", "cyber"]
game = Hangman(word_list, max_attempts=6)

# Play the game
while not game.is_game_over():
    print(game.get_masked_word())
    print(f"Attempts left: {game.get_attempts_left()}")
    letter = input("Enter a letter: ")
    game.guess_letter(letter)

# Print the game result
if game.get_attempts_left() > 0:
    print("Congratulations! You guessed the word correctly.")
else:
    print("Game over! You ran out of attempts.")