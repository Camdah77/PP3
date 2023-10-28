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
        quit()


def rightdoor():
    print("\n Nice! You are closer to the freedom. You now need a cod to enter your second door")
    rightroom_code = input("The code is: 23 - 13 + 4? Type thr code?  :")
    rightroom_correct = 14

    if int(rightroom_code) == rightroom_correct: 
        {level2()}
           
    else:
        print("Sorry, that's not correct.The code was:", rightroom_correct)
        quit()

def level2():
    name = input("What is your name?")
    name_length = len(name)
    print(f"Your name contains {name_length} letters")
    
    namequiz = ((name_length * 10)-50 + 20)
    nameans = input("If we multiply your letters with 10, subtract 50 and add 20. What we have left?  ")

    if int(nameans) == namequiz: 
     {level3()}
           
    else:
        print("Sorry, that's not correct.The answer was:", namequiz)
        quit()

def level3():
    print("welcome to level 3")

def quit():
    print("You have to stay in the museum until somebody is coming...")
    sys.exit(0)

if __name__ == "__main__":
    startlevel()
    level2()
    level3()
