import random
import sys
from termcolor import colored
import art


# Welcome message with logo and instructions how to play
print(colored("Welcome to", "white"))

print(colored("ESCAPE FROM THE MUSEUM", "red"))
art.welcome_logo()
print("\n")
print("You are all alone in a museum.\n" 
"All the doors are locked.\n" 
"\n Solve the steps to reach the freedom\n")


#Starts the game


def startlevel():
    print(colored("You have two doors in front of you.", 'green'))
    print(colored("One door is taking you to the a dark basement.", 'green'))
    print(colored("And one door is taking you one step closer to the freedom", 'magenta'))
    print(colored("Which door do you enter?", 'yellow'))

#Calling ASCII - Art from art.py
    art.key()
    print("\n 1. Left door ")
    print("\n 2. Right door")
    doorchoice = input(colored("\nType 1 or 2 to make a choice:  ", 'yellow'))

#Two choice for user
    if doorchoice == "1":
        leftdoor()
    elif doorchoice == "2":
        rightdoor()
    else:
       print(colored(f"Please enter 1 och 2", "red"))
    play_again()

#Left door function


def leftdoor():
    print("\n Left door was a good choice!")
    print("\nThe second door also needs a code:")

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 50)

    leftroom_code = num1 - num2

    print(colored(f"What is {num1} - {num2} ?", 'yellow'))  
    leftroom_ans = input("Type the code: ")

    if leftroom_ans == str(leftroom_code):
        print(colored("Correct!\n", 'magenta'))
        level2()
    else:
        print(colored("Wrong code. The door remains locked", 'red'))
        play_again()


#Right door function


def rightdoor():
    print("\nYou made a very good choice.")
    print("\nThe second door also needs a code:")

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 50)

    rightroom_code = num1 - num2

    print(f"What is {num1} - {num2} ?")  
    rightdoor_ans = input("Type the code: ")

    if rightdoor_ans == str(rightroom_code):
        print(colored("Correct!\n", 'magenta'))
        level2()

    else:
        print(colored("Wrong code. The door remains locked", 'red'))
        play_again()


#Level 2 function

def level2():
    art.fire()
    name = input(colored("\nVery good! To open the third door, you have to enter your name: ", 'magenta'))
    name_length = len(name)
    print(f"Your name contains {name_length} letters")

    namequiz = ((name_length * 10) - 50 + 20)
    nameans = input(colored(f"\nIf we multiply {name_length} by 10," 
    "subtract 50, and add 20, what do we have left? ", 'yellow'))

    if nameans == str(namequiz):
        print(colored("Correct!\n", 'magenta'))
        level3()

    else:
        print(colored("Wrong code. The door remains locked. The code is: {namequiz}.", 'red'))
        play_again()

        
#Level 3 with random numbers to addition


def level3():
    print("\nYour are brilliant in math")
    print("\nYou now ony have two doors left:")
    
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
   
    level3_code = num1 * num2

    print(colored(f"What is {num1}*{num2}?", 'yellow'))
    level3_ans = input("Type the your answer: ")

    if level3_ans == str(level3_code):
        print(colored("Correct!\n", 'magenta'))
        level4()

    else:
        print(colored("Wrong code. The door remains locked ", 'red'))
        play_again()

#Level 4 with 4 questions


def level4():
    print(colored(f"Welcome to the final door", 'green'))
    print("\nCan you solve the code for last door? ")
   
    print(colored("1:If January is month  nr 1: what number is July", 'red'))
    print(colored("2: What is 18 - 10", 'yellow'))
    print(colored("3: If A is number 1. What is F?", 'red'))
    print(colored("4: The sum of: 23 + 21 + 200 + 12 + 22 + 8 + 12 + 5 multiplied by 0?", 'yellow'))

    code_final = 7860
    tries = 3  # Number of allowed tries

    while tries > 0:
        code_attempt = input("\nEnter the code: ")

        if code_attempt.isdigit() and len(code_attempt) == 4:
            code_attempt = int(code_attempt)
            if code_attempt == code_final:
                print(colored(f"CONGRATULATIONS ! You made it!!!\n", 'green'))
                sys.exit(0)

            else:
                tries -= 1
                if tries > 0:
                    print(f"Wrong code! You have {tries} {'tries' if tries > 1 else 'try'} left")
                else:
                    print(f"Too bad, {name}! You've used all your attempts. Game over.")
                    play_again()
        else:
            print(colored("Invalid input. Please enter a 4-digit number.", 'yellow'))


#Allow user to play agian


def play_again():
    play_again = input("You didn't make it this time. Do you want to play again? (Y / N): ").strip().lower()
    if play_again == "y":
        startlevel()  # Restart the game
    else:
        print("Sorry... You have to stay in the museum until somebody comes...")
        sys.exit(0)

if __name__ == "__main__":
    startlevel()