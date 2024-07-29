# Your Task
# Your task is to create a simple Book class. This class should have two attributes: title and author.

# You will need to define an __init__ method to initialize these attributes when a new Book instance is created.

# Then, instantiate an object of the Book class and print out its title and author.

# Example Usage
# After completing your Book class, you should be able to use it as follows:

# my_book = Book(title="To Kill a Mockingbird", author="Harper Lee")
# print(my_book.title)  # Output: To Kill a Mockingbird
# print(my_book.author) # Output: Harper Lee
# Guidelines
# Make sure your Book class has an __init__ method that accepts title and author as parameters and initializes 
# the respective attributes.
# Use the instance variables self.title and self.author to store the title and author passed to the __init__ method.
# When printing the book's title and author, ensure that the output matches the example usage provided above.
# Remember to follow the PEP 8 style guide for Python code to ensure your code is clean and readable.

class Book:
    def __init__(self, title, author):
        '''
        Initializes the Book class with title and author attributes.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        '''
        self.title = title
        self.author = author


my_book = Book(title="To Kill a Mockingbird", author="Harper Lee")
print(my_book.title)  
print(my_book.author)