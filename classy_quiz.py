# Requirements
# Your task is to design a set of classes that collectively form the foundation of a quiz system.

# The system should allow for creating quizzes with multiple-choice questions, presenting these questions to the user, and then scoring the quiz
# based on the user's answers.

# 1. Question Class
# Purpose: Represents a single quiz question, including the question text, a list of possible answers, and the correct answer.
# Required Attributes:
# text: The text of the question.
# choices: A list of possible answers.
# answer: The correct answer from the choices.
# 2. Quiz Class
# Purpose: Manages a collection of Question objects, tracks the user's score, and controls the flow of the quiz.
# Required Attributes:
# questions: A list of Question objects.
# __current_index: An integer representing the index of the current question.
# score: An integer score starting at 0.
# Required Methods:
# Method to present the current question to the user and accept their answer.
# Method to move to the next question.
# Method to calculate and display the final score.
# Exercise Tasks
# Design and implement the Question class according to the requirements.
# Design and implement the Quiz class that uses instances of the Question class.
# Create a small set of questions and use them to instantiate a Quiz object.
# Develop a simple function that serves as an interactive command-line interface that allows the user to take the quiz, select answers, 
# and see their final score.
# Tips
# Think about how each class interacts with the others and how you can use encapsulation to keep each class focused on a single responsibility.
# Test your classes individually before integrating them into the quiz application.

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.__current_index = 0
        self.score = 0

    def present_question(self):
        question = self.questions[self.__current_index]
        print(question.text)
        for i, choice in enumerate(question.choices, 1):
            print(f"{i}. {choice}")

    def next_question(self):
        self.__current_index += 1
    
    def check_answer(self, choice):
        question = self.questions[self.__current_index]
        if question.choices[choice-1] == question.answer:
            self.score += 1

    def final_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")

# Sample questions
q1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris")
q2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], "4")
q3 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars")

questions = [q1, q2, q3]
quiz = Quiz(questions)

while quiz._Quiz__current_index < len(questions):
    quiz.present_question()
    choice = int(input("Enter the number of your choice: "))
    quiz.check_answer(choice)
    quiz.next_question()

quiz.final_score()