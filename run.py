import gspread
from google.oauth2.service_account import Credentials
from datetime import date
import datetime
import random
import operator as op
import time
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('math')

print("ESCAPE FROM THE MUSEUM")
print("You are all alone in a museum.\n "  "All the doors are locked.\n " "You need a key to get out. \n" "Your mission enter five locked door to find the key.\n")


def get_choice(options):
    valid_choice = False
    while not valid_choice:
        print("\n Your alternatvies:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Make a choice, please: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                valid_choice = True
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")
    return choice

def startlevel():
    print("You have two doors in front of you.")
    while True:
        choice = get_choice(["Left door", "Right door"])
        if choice == 1:
            {leftdoor()}
        elif choice == 2:
            print("Nice! You are closer to the freedom")
            {rightdoor()}

def leftdoor():
    print("\n After you entered the left door and you now need a code to pass door nr 2")
    leftroom_code = input("The code is: half of two plus two? Type your answer  :")
    leftdoor_correct = 3

    if int(leftroom_code) == leftdoor_correct : 
        {level2()}
        valid_choice = False
    else:
        print("Sorry, that's not correct.")
        exit_program()


def rightdoor():
    print("\n Nice! You are closer to the freedom. You now need a cod to enter your second door")
    rightroom_code = input("The code is: 23 - 13 + 4? Type thr code?  :")
    rightroom_correct = 14

    if int(rightroom_code) == rightroom_correct: 
        {level2()}
        valid_choice = False
    
    else:
        print("Sorry, that's not correct.The code was:", rightroom_correct)
        exit_program()

def level2():
        # Generate a random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 100)

     
print("Correct! Answer three questions to enter next door. ")

print(num1, "+", num3 )
user_answer1 = int(input("Your answer: "))

print(num2, "*", num3,)
user_answer2 = int(input("Your answer: "))

print(num3, "-", num1,)
user_answer3 = int(input("Your answer: "))

# Check answers
if user_answer1 == num1 + num3:
    print("Question 1: Correct ")
else:
    print("Question 1: wrong answer")

if user_answer2 == num2 * num3:
    print("Question 2: Correct")
else:
    print("Question 2: wrong answer")

if user_answer3 == num3 - num1:
    print("Question 3: Correct")
else:
    print("Question 3: wrong answer")






def exit_program():
    print("You have to stay in the museum until somebody is coming...")
    sys.exit(0)

if __name__ == "__main__":
    startlevel()
    leftdoor()
    rightdoor()
    level2()