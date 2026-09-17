#imports
import os
import re
import subprocess
import sys
from pathlib import Path
import unicodedata
from time import sleep

#clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

#Logos for the main menu and the modules
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
        [4] - IP Tracker        [SOON]   [5] - Domain Searcher [Work]      [6] - Social Media Searcher [SOON]

        
                
        [99] - Exit
        [999] - Credits                                                                                 [???]???
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

EMAILSEARCHER = r"""
 ██████████                            ███  ████              █████████                                        █████                        
░░███░░░░░█                           ░░░  ░░███             ███░░░░░███                                      ░░███                         
 ░███  █ ░  █████████████    ██████   ████  ░███            ░███    ░░░   ██████   ██████   ████████   ██████  ░███████    ██████  ████████ 
 ░██████   ░░███░░███░░███  ░░░░░███ ░░███  ░███  ██████████░░█████████  ███░░███ ░░░░░███ ░░███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
 ░███░░█    ░███ ░███ ░███   ███████  ░███  ░███ ░░░░░░░░░░  ░░░░░░░░███░███████   ███████  ░███ ░░░ ░███ ░░░  ░███ ░███ ░███████  ░███ ░░░ 
 ░███ ░   █ ░███ ░███ ░███  ███░░███  ░███  ░███             ███    ░███░███░░░   ███░░███  ░███     ░███  ███ ░███ ░███ ░███░░░   ░███     
 ██████████ █████░███ █████░░████████ █████ █████           ░░█████████ ░░██████ ░░████████ █████    ░░██████  ████ █████░░██████  █████    
░░░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░             ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░                                                                                                                                        
"""

PHONESEARCHER = r"""
 ███████████  █████                                                 ███████             ███              █████   
░░███░░░░░███░░███                                                ███░░░░░███          ░░░              ░░███    
 ░███    ░███ ░███████    ██████  ████████    ██████             ███     ░░███  █████  ████  ████████   ███████  
 ░██████████  ░███░░███  ███░░███░░███░░███  ███░░███ ██████████░███      ░███ ███░░  ░░███ ░░███░░███ ░░░███░   
 ░███░░░░░░   ░███ ░███ ░███ ░███ ░███ ░███ ░███████ ░░░░░░░░░░ ░███      ░███░░█████  ░███  ░███ ░███   ░███    
 ░███         ░███ ░███ ░███ ░███ ░███ ░███ ░███░░░             ░░███     ███  ░░░░███ ░███  ░███ ░███   ░███ ███
 █████        ████ █████░░██████  ████ █████░░██████             ░░░███████░   ██████  █████ ████ █████  ░░█████ 
░░░░░        ░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░                ░░░░░░░    ░░░░░░  ░░░░░ ░░░░ ░░░░░    ░░░░░  
"""

IPTRACKER = r"""
 █████ ███████████             ███████████                              █████                        
░░███ ░░███░░░░░███           ░█░░░███░░░█                             ░░███                         
 ░███  ░███    ░███           ░   ░███  ░  ████████   ██████    ██████  ░███ █████  ██████  ████████ 
 ░███  ░██████████  ██████████    ░███    ░░███░░███ ░░░░░███  ███░░███ ░███░░███  ███░░███░░███░░███
 ░███  ░███░░░░░░  ░░░░░░░░░░     ░███     ░███ ░░░   ███████ ░███ ░░░  ░██████░  ░███████  ░███ ░░░ 
 ░███  ░███                       ░███     ░███      ███░░███ ░███  ███ ░███░░███ ░███░░░   ░███     
 █████ █████                      █████    █████    ░░████████░░██████  ████ █████░░██████  █████    
░░░░░ ░░░░░                      ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
"""

SOCIALSEARCHER = r"""
  █████████                     ███            ████              █████████                                        █████     
 ███░░░░░███                   ░░░            ░░███             ███░░░░░███                                      ░░███      
░███    ░░░   ██████   ██████  ████   ██████   ░███            ░███    ░░░   ██████   ██████   ████████   ██████  ░███████  
░░█████████  ███░░███ ███░░███░░███  ░░░░░███  ░███  ██████████░░█████████  ███░░███ ░░░░░███ ░░███░░███ ███░░███ ░███░░███ 
 ░░░░░░░░███░███ ░███░███ ░░░  ░███   ███████  ░███ ░░░░░░░░░░  ░░░░░░░░███░███████   ███████  ░███ ░░░ ░███ ░░░  ░███ ░███ 
 ███    ░███░███ ░███░███  ███ ░███  ███░░███  ░███             ███    ░███░███░░░   ███░░███  ░███     ░███  ███ ░███ ░███ 
░░█████████ ░░██████ ░░██████  █████░░████████ █████           ░░█████████ ░░██████ ░░████████ █████    ░░██████  ████ █████
 ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░  ░░░░░░░░ ░░░░░             ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░░ 
"""

#colors for the logos
CYAN = '\033[96m'
BLUE = '\033[94m'
RED = '\033[91m'

#print the main logo
print(f"{CYAN}{LOGO}{CYAN}")

#loads the social searcher
def Social_searcher():

    #clear screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #Print the social searcher logo
    print(f"{RED}{SOCIALSEARCHER}{RED}")
    print("Please wait while loading the social searcher..")
    sleep(5)
    print("Success")

#loads the domain searcher module
def Domain_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #Loads the tool
    print("Please wait while loading the domain searcher...")
    domain_module = (
        Path(__file__).resolve().parent
        / "MODULES"
        / "CATEGORIES"
        / "Domain_search"
        / "domain_methods.py"
    )
    subprocess.run([sys.executable, str(domain_module)], check=False)

#Load the Ip tracker module
def Ip_tracker():
    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the IP tracker logo
    print(f"{BLUE}{IPTRACKER}{BLUE}") #Print the IP tracker logo
    print("Please wait while loading the IP tracker...")
    sleep(5) 
    print("Success")

#load the phone module
def Phone_searcher():
    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the phone number searcher logo
    print(f"{BLUE}{PHONESEARCHER}{BLUE}")
    print("Please wait while loading the phone number searcher...")
    sleep(5)
    print("Success")

#load the email module
def email_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the email searcher logo
    print(f"{BLUE}{EMAILSEARCHER}{BLUE}")
    print("Please wait while loading the email searcher...")
    sleep(5)
    print("Success")

#username function
def user_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the username searcher logo
    print(f"{BLUE}{USERSEARCHER}{BLUE}")
    print("Please wait while loading the username searcher...")
    sleep(5)
    print("Success")

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