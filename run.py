import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('math')

def get_userinput():
    
    """
    Get name and age from user.
    If user is under 8: level 1
    If user is under 13: level 2
    If youser is over 15: lever 3
    """
    print("Welcome to math adventure")
    
    name = input("What is your name?: ")
    print(f"Hi {name}")

    age = input("How old are you?: ")
    print(f"{age}")

        

get_userinput()