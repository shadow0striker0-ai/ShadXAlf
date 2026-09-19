#imports
from pathlib import Path
from time import sleep
import os
import sys
import subprocess

# Make the project package importable when this file is launched directly.
project_root = Path(__file__).resolve().parents[3]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

#externall calls
from MODULES.CATEGORIES.Dark_site.C.U.modules import (
    MONEY_MAKER
)

#clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

#logo
MENU = r"""
           █████████  █████                    █████ █████ █████   █████████   ████     ██████     
          ███░░░░░███░░███                    ░░███ ░░███ ░░███   ███░░░░░███ ░░███    ███░░███    
         ░███    ░░░  ░███████    ██████    ███████  ░░███ ███   ░███    ░███  ░███   ░███ ░░░     
         ░░█████████  ░███░░███  ░░░░░███  ███░░███   ░░█████    ░███████████  ░███  ███████       
          ░░░░░░░░███ ░███ ░███   ███████ ░███ ░███    ███░███   ░███░░░░░███  ░███ ░░░███░        
          ███    ░███ ░███ ░███  ███░░███ ░███ ░███   ███ ░░███  ░███    ░███  ░███   ░███         
         ░░█████████  ████ █████░░████████░░████████ █████ █████ █████   █████ █████  █████        
          ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░   ░░░░░ ░░░░░  ░░░░░         
                                                                                                   
 ██████████ ██████████ ██████████ ██████████ ██████████ ██████████ ██████████ ██████████ ██████████
░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ 
                                                                                                   
 ██████████     █████████   ███████████   █████   ████     █████████  █████ ██████████   ██████████
░░███░░░░███   ███░░░░░███ ░░███░░░░░███ ░░███   ███░     ███░░░░░███░░███ ░░███░░░░███ ░░███░░░░░█
 ░███   ░░███ ░███    ░███  ░███    ░███  ░███  ███      ░███    ░░░  ░███  ░███   ░░███ ░███  █ ░ 
 ░███    ░███ ░███████████  ░██████████   ░███████       ░░█████████  ░███  ░███    ░███ ░██████   
 ░███    ░███ ░███░░░░░███  ░███░░░░░███  ░███░░███       ░░░░░░░░███ ░███  ░███    ░███ ░███░░█   
 ░███    ███  ░███    ░███  ░███    ░███  ░███ ░░███      ███    ░███ ░███  ░███    ███  ░███ ░   █
 ██████████   █████   █████ █████   █████ █████ ░░████   ░░█████████  █████ ██████████   ██████████
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░     ░░░░░░░░░  ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░

        [01] - Money-Making [In Progress]
        [99] - return To Main Menu
"""

#color
RED = "\033[91m"

#print the panner
print(f"{RED}{MENU}{RED}")

#returns
def GET_BACK():
    sys.exit(0)


#main menu
def main():

    #user input
    USER_INPUT = input("Enter (1) to continue~ ")

    #enter setup
    if USER_INPUT == "1":
        MONEY_MAKER()

    #return to main menu
    elif USER_INPUT == "99":
        GET_BACK()

    #fallback invalid choice
    else:
        print("Invalid choice")

# Main entrance.
if __name__ == "__main__":
    main()