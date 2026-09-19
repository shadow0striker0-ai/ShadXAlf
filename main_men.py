#imports
import os
import re
import subprocess
import sys
from pathlib import Path
import unicodedata
from time import sleep
from MODULES.UTILITIES.ascii import (
    CYAN,
    COLORRESET, 
    BLUE, 
    RED, 
    LOGO, 
    SOCIALSEARCHER, 
    IPTRACKER, 
    PHONESEARCHER, 
    EMAILSEARCHER, 
    USERSEARCHER,
    DOMAINSEARCHER
)
from MODULES.CATEGORIES.modules import *

#clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
        return
    else:
        os.system('clear')
        return
clear_screen()


#print the main logo
print(f"{CYAN}{LOGO}{COLORRESET}")


def User

#Loads the Domain Searcher
def Domain_searcher():

    #clear screen
    clear_screen()

    print(f"{BLUE}{DOMAINSEARCHER}{COLORRESET}")

    #Loading Animation for Module Loading
    for dot_count in range(1, 10):
        print(f"\rDomain Searcher is loading{'.' * dot_count}", end="", flush=True)
    sleep(0.5)

    #run the module
    Domain_Script = Path(__file__).resolve().parent.parent / "Domain_search" / "Domain_methods.py"
    subprocess.run([sys.executable, str(Domain_Script)], check=False)



#Main Menu
def main():

    #filter the input to only allow numbers and remove any escape sequences
    raw_choice = input("Enter your choice: ")
    clean_choice = re.sub(r"\x1b\[[0-9;?]*[ -/]*[@-~]", "", raw_choice)
    normalized_choice = unicodedata.normalize("NFKC", clean_choice)
    choice = "".join(
        character for character in normalized_choice if character in "0123456789"
        )
    
    #categorie 1
    if choice == "1":
        user_searcher() # hop into the username searcher function

    #categorie 2
    elif choice == "2":
        email_searcher() # hop into the email searcher function

    #categorie 3
    elif choice == "3":
        Phone_searcher() # hop into the phone number searcher function

    #categorie 4
    elif choice == "4":
        Ip_tracker() # hop into the IP tracker function

    #categorie 5
    elif choice == "5":
        Domain_searcher() # hop into the domain searcher function

    #categorie 6
    elif choice == "6":
        Social_searcher() #hop into social searcher

    #exit function
    elif choice == "99":
        print("Exiting...")
        sleep(2)
        sys.exit(0)

    #show credits
    elif choice == "999":
        credits_script = Path(__file__).resolve().parent / "MODULES" / "CREDITS" / "show_credits.py"
        subprocess.run([sys.executable, str(credits_script)], check=False)
        clear_screen()
        print(f"{CYAN}{LOGO}{CYAN}")

    #loads hidden feature
    elif choice == bytes.fromhex("363636").decode("ascii"):
        hidden_script = Path(__file__).resolve().parent.parent / "Dark_site" / "pre_setup.py"
        subprocess.run([sys.executable, str(hidden_script)], check=False)

    #instant leave
    else:
        print("Invalid choice. Please try again.")
        print("Exiting...")
        sleep(2)
        sys.exit(0)

#main entrance
if __name__ == "__main__":
    main()