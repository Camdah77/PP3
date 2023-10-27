import gspread
from google.oauth2.service_account import Credentials
from datetime import date
import datetime
import random
import operator as op

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('math')

print("Welcome to math challenge")
print("\n")
print("This game has two level")
print("Level 1: Contains addition and subtraction")
print("Level 2: Contains addition, subtraction, division and multiplication")
print("The number of questions is based on your age")
print("\n")


def get_userinfo():
    name = input("What is your name?")
    age = input("How old are you?")
operator = random.choice(['+', '-', '*', '/'])

levels = {
    "1": operator['+'],
    "2": operator['+', '-'],
    "3": operator['+', '-', '*', '/']
}

def select_level():
    print("Levels:")
    for name, level in levels.items(): 
        print("{}: {}".format(name, level))
    print("")
    name = input("Choose level: ")
    while name not in LEVELS:
        print("Not a valid choice!")
        name = input("Choose level:")
    return LEVELS[name]

def addition(self):
        """
        Addition for level 1-3
        Question & answer
        """
 
        # Generating two random numbers between 1 and 10.
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
 
        # Creating the question string.
        question = f"What is {num1} + {num2}?"
 
        # Calculating the correct answer.
        answer = num1 + num2
 
        return question, answer

def subtraction(self):
        """
        subtraction for level 1-3
        Question & answer
        """
 
        # Generating two random numbers between 1 and 10.
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
 
        # Creating the question string.
        question = f"What is {num1} - {num2}?"
 
        # Calculating the correct answer.
        answer = num1 - num2
 
        return question, answer

def division(self):
        """
        division for level 3
        Question & answer
        """
 
        # Generating two random numbers between 1 and 10.
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
 
        # Creating the question string.
        question = f"What is {num1} / {num2}?"
 
        # Calculating the correct answer.
        answer = num1 / num2
 
        return question, answer

def multiplication(self):
        """
        multiplication for level 3
        Question & answer
        """
 
        # Generating two random numbers between 1 and 10.
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
 
        # Creating the question string.
        question = f"What is {num1} * {num2}?"
 
        # Calculating the correct answer.
        answer = num1 * num2
 
        return question, answer
 
 if __name__ == "__main__":
    num_questions = (f'{age}')
    LEVELS = select_level()
    game = MathGame(num_questions)
    game.play()
