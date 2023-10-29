import gspread
from google.oauth2.service_account import Credentials
import random
import sys
from termcolor import colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('math')

print(colored("ESCAPE FROM THE MUSEUM", "red", attrs=["blink"]))

print("You are all alone in a museum.\n" "All the doors are locked.\n" "\n Solve the steps to win the game\n")


def startlevel():
    print(colored("You have two doors in front of you.",'green' ))
    print(colored("Which door do you enter?", 'magenta' ))
    print("\n 1. Left door")
    print("\n 2. Right door")
    doorchoice = input("\nType 1 or 2, to make a choice: " )
    
    if int(doorchoice) == 1:
        leftdoor()  # passing the user to the left door
    elif int(doorchoice) == 2:
        rightdoor()  # passing the user to the right door

def leftdoor():
    print("\n Great! You now need a code to enter your second door")
    print (colored("\n code=(a+b)2   | a=5 | b=2", 'magenta'))
    leftroom_code = input("\nWhat is the code?  ")
    leftdoor_correct = 14

    if int(leftroom_code) == leftdoor_correct : 
        level2() # Passing to level2

    else:
        print("Sorry, that's not correct.")
        quit()


def rightdoor():
    print("\n Nice! 45 to enter your second door")
    print(colored("\n code=(a-b)5 | a=15 | b=6.", 'magenta'))
    rightroom_code = input("\nWhat is the code?  ")
    rightroom_correct = 45

    if int(rightroom_code) == rightroom_correct: 
        level2() # Passing to level2
           
    else:
        print("Sorry, that's not correct.The code was:", rightroom_correct)
        quit()

def level2():
    name = input(colored("\nVery good! To open the third door, you have to enter your name: ", 'magenta'))
    name_length = len(name)
    print(f"Your name contains {name_length} letters")
    
    namequiz = ((name_length * 10) - 50 + 20)
    nameans = input(colored(f"\nIf we multiply {name_length} by 10, subtract 50, and add 20, what do we have left? ",'cyan'
 ))
    
    if int(nameans) == namequiz:
        level3(name)  # Send user name to next level

    else:
        print("Sorry, that's not correct. The answer was:", namequiz)
        quit()

def level3(name):
    print(colored("Welcome to your final door, " + name ,'magenta'))
    print("\n To open the final door, you need to type a secret code of four numbers")

    print(colored("1: January is month number 1. What is May?", 'red'))
    print(colored("\n 2: How many planets are there in the solar system?", 'yellow' ))
    print(colored("\n 3: If A is number 1. What is F?", 'red' ))
    print(colored("\n 4 The sum of: 23 + 21 + 200 + 12 + 22 + 8 + 12 + 5 multiplyed with 0?",'yellow' ))

    code_final = 5860
    tries = 3  # Number of allowed tries

    while tries > 0:
        code_attempt = input("\nEnter the code: ")

           
        if code_attempt.isdigit() and len(code_attempt) == 4:
            code_attempt = int(code_attempt)
            if code_attempt == code_final:
                print(colored("CONGRATULATIONS  " + name + "! You made it!!! \n", 'light_red'	))
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