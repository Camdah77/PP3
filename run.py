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
print("You are all alone in a museum.\n "  "All the doors are locked.\n " "You need a key to get out. \n" "Your mission: find the key by solving clued (1-5 steps - if you are lucky ).\n")


def startlevel():
    print("You have two doors in front of you.")
    print("One is to the left and one is to the right")
    print("\n 1. Left door")
    print("\n 2. Right door")
    doorchoice = input("\nType 1 or 2, to make a choice: " )
    
    if int(doorchoice) == 1:
        leftdoor()  # passing the user to the left door
    elif int(doorchoice) == 2:
        rightdoor()  # passing the user to the right door

def leftdoor():
    print("\n Great! You now need a code to enter your second door")
    print("\n code=(a+b)2   | a=5 | b=2")
    leftroom_code = input("\nWhat is the code?  ")
    leftdoor_correct = 14

    if int(leftroom_code) == leftdoor_correct : 
        level2() # Passing to level2

    else:
        print("Sorry, that's not correct.")
        quit()


def rightdoor():
    print("\n Nice! 45 to enter your second door")
    print("\n code=(a-b)5 | a=15 | b=6.")
    rightroom_code = input("\nWhat is the code?  ")
    rightroom_correct = 45

    if int(rightroom_code) == rightroom_correct: 
        level2() # Passing to level2
           
    else:
        print("Sorry, that's not correct.The code was:", rightroom_correct)
        quit()

def level2():
    name = input("\nVery good! To open the third door, you have to enter your name: ")
    name_length = len(name)
    print(f"Your name contains {name_length} letters")
    
    namequiz = ((name_length * 10) - 50 + 20)
    nameans = input(f"\nIf we multiply {name_length} by 10, subtract 50, and add 20, what do we have left? ")
    
    if int(nameans) == namequiz:
        level3(name)  # Send user name to next level

    else:
        print("Sorry, that's not correct. The answer was:", namequiz)
        quit()

def level3(name):
    print("Welcome to your final door, " + name)
    print("\n To open the final door, you need to type a secret code with four numbers")

    print("1: January is month number 1. What is May? ")
    print("\n 2: How many planets are there in the solar system?")
    print("\n 3: If A is number 1. What is F?")
    print("\n 4 The sum of: 23 + 21 + 200 + 12 + 22 + 8 + 12 + 5 multiplyed with 0?")

    code_final = 5860
    tries = 3  # Number of allowed tries

    while tries > 0:
        code_attempt = input("\nEnter the code: ")

           
        if code_attempt.isdigit() and len(code_attempt) == 4:
            code_attempt = int(code_attempt)
            if code_attempt == code_final:
                print("CONGRATULATIONS  " + name + "! You made it!!! \n")
                break  # Exit the loop

            else:
                tries -= 1
                if tries > 0:
                    print(f"Wrong code! You have {tries} {'tries' if tries > 1 else 'try'} left")
                    
                else:
                    print("To bad " + name + " You've used all your attempts. Game over.")
                    break
        else:
            print("Invalid input. Please enter a 4-digit number.")
    


def quit():
    play_again = input("You did´n make it this time. Do you want to play again? (Y / N ): ").strip().lower()
    if play_again == "Y" or "y":
        startlevel()  # Restart the game
    else:
        print("Sorry....You have to stay in the museum until somebody is coming...")
        sys.exit(0)

if __name__ == "__main__":
    startlevel()