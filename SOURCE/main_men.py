#imports
import os
import re
import subprocess
from pathlib import Path
import unicodedata
from time import sleep


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

LOGO = r"""
                        ███████╗██╗  ██╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██╗     ███████╗                                 
                        ██╔════╝██║  ██║██╔══██╗██╔══██╗╚██╗██╔╝██╔══██╗██║     ██╔════╝                                 
                        ███████╗███████║███████║██║  ██║ ╚███╔╝ ███████║██║     █████╗                                   
                        ╚════██║██╔══██║██╔══██║██║  ██║ ██╔██╗ ██╔══██║██║     ██╔══╝                                   
                        ███████║██║  ██║██║  ██║██████╔╝██╔╝ ██╗██║  ██║███████╗██║                                      
                        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝                                      
                
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗ 
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ 
                                                                                                                                                                                                                                                  
 ██████╗ ███████╗██╗███╗   ██╗████████╗    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██║   ██║███████╗██║██╔██╗ ██║   ██║       █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██║   ██║╚════██║██║██║╚██╗██║   ██║       ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
╚██████╔╝███████║██║██║ ╚████║   ██║       ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

        [1] - Username Searcher [SOON]   [2] - Email Searcher  [SOON]      [3] - Phone Number Searcher [SOON]
        [4] - IP Tracker        [SOON]   [5] - Domain Searcher [SOON]      [6] - Social Media Searcher [SOON]

        
                
        [99] - Exit
        [999] - Credits
 
 
 """

USERSEARCHER = r"""
 █████  █████                                                                                     █████                        
░░███  ░░███                                                                                     ░░███                         
 ░███   ░███   █████   ██████  ████████              █████   ██████   ██████   ████████   ██████  ░███████    ██████  ████████ 
 ░███   ░███  ███░░   ███░░███░░███░░███ ██████████ ███░░   ███░░███ ░░░░░███ ░░███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
 ░███   ░███ ░░█████ ░███████  ░███ ░░░ ░░░░░░░░░░ ░░█████ ░███████   ███████  ░███ ░░░ ░███ ░░░  ░███ ░███ ░███████  ░███ ░░░ 
 ░███   ░███  ░░░░███░███░░░   ░███                 ░░░░███░███░░░   ███░░███  ░███     ░███  ███ ░███ ░███ ░███░░░   ░███     
 ░░████████   ██████ ░░██████  █████                ██████ ░░██████ ░░████████ █████    ░░██████  ████ █████░░██████  █████    
  ░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░                ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
"""


import subprocess
import sys

CYAN = '\033[96m'
BLUE = '\033[94m'

print(f"{CYAN}{LOGO}{CYAN}")





#username function
def user_searcher():
    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(f"{BLUE}{USERSEARCHER}{BLUE}")
    print("Please wait while loading the username searcher...")
    sleep(5)
    return


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
        user_searcher()
    #categorie 2
    elif choice == "2":
        print("Email Searcher is coming soon!")
        sleep(2)
    #categorie 3
    elif choice == "3":
        print("Phone Number Searcher is coming soon!")
        sleep(2)
    #categorie 4
    elif choice == "4":
        print("IP Tracker is coming soon!")
        sleep(2)
    #categorie 5
    elif choice == "5":
        print("Domain Searcher is coming soon!")
        sleep(2)
    #categorie 6
    elif choice == "6":
        print("Social Media Searcher is coming soon!")
        sleep(2)
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
    else:
        print("Invalid choice. Please try again.")
        print("Exiting...")
        sleep(2)
        sys.exit(0)


if __name__ == "__main__":
    main()