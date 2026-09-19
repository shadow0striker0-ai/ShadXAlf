#imports
import os
import subprocess
import sys
from pathlib import Path

# Make the project package importable when this file is launched directly.
project_root = Path(__file__).resolve().parents[6]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

#external ccalling
from MODULES.CATEGORIES.Dark_site.C.U.ascii import (
    DEEEP,
    RESET,
    PCH,
)

# Clear the terminal before showing the menu.
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#return method
def GET_BACK():
    sys.exit(0)

#UI
def main():

    # Clear the screen before rendering the menu.
    clear_screen()

    #show banner
    print(f"{DEEEP}{PCH}{RESET}")

    #user input
    user_input = input("Enter your Option~ ")

    #option 1 placeholder
    if user_input == "1":
        print("Test worked")

    #option to exit
    elif user_input == "99":
        GET_BACK()

    #fallback
    else:
        print("Invalid choice")
        print("LEAVING!...")
        sys.exit(0)


if __name__ == "__main__":
    main()





