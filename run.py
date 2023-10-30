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
    while doorchoice 
#Left door function with addition


def leftdoor():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
      
    leftroom_code = num1 + num2

    print("\n You made a very good choice. ")
    print("\n The second door need a code: ")
    leftdoor_quest =(f"What is {num1} + {num2}?",'yellow')
    leftdoor_ans = input(" Your answer: ")

    if leftdoor_ans == str(leftdoor_ans):
            print("Correct!\n")
            level2()
    else:
            print(f"Wrong code. The door remains locked")
            play_again()
  

#Right door function33 with subtraction


def rightdoor():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 50)

    rightroom_code = num1 - num2
    
    print("\n You made a very good choice. ")
    print("\n The second door need a code: ")
    
    rightdoor_quest = f"What is {num1} + {num2}?"
    print(rightdoor_quest)
    rightdoor_ans = input(rightdoor_quest + " Your answer: ")

    if rightdoor_ans == str(rightdoor_quest):
            print("Correct!\n")
            level2()
    else:
            print(f"Wrong code. The door remains locked")
            play_again()


#Level 2 with name input function


def level2():
    art.fire()
    name = input(colored("\nVery good! To open the third door, you have to enter your name: ", 'magenta'))
    name_length = len(name)
    print(f"Your name contains {name_length} letters")

    namequiz = ((name_length * 10) - 50 + 20)
    nameans = input(colored(f"\nIf we multiply {name_length} by 10," 
    "subtract 50, and add 20, what do we have left? ", 'cyan'))

    if nameans == str(namequiz):
        print(colored("Correct!\n", 'yellow'))
        level3()

    else:
        print("Sorry, that's not correct.")
        play_again()


#Level 3 with random numbers to addition


def level3():
    print("\n Well done- But antoher code infront of you! ")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 50)

    lev3answer = num1 + num2
    level3question = f"What is {num1} + {num2}?"
    user_answer = input(" Your answer: ")

    if user_answer == str(lev3answer):
            print("Correct!\n")
            level4(user_answer)
    else:
            print(f"Sorry, the correct answer is  {lev3answer}.\n")
            play_again()


#Level 4 with 4 questions


def level4(name):
    print(colored(f"Welcome to your final door, {name}!", 'magenta'))
    print("\nTo open the final door, "
    "you need to type a secret code of four numbers")

    print(colored("1:If January is month  nr 1: what number is July", 'red'))
    print(colored("2: What is 18 - 10"))
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