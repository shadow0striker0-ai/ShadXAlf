import os

from pathlib import Path
import subprocess
import sys
from time import sleep
from MODULES.UTILITIES.ascii import (
    CYAN, 
    BLUE, 
    RED, 
    LOGO, 
    SOCIALSEARCHER, 
    IPTRACKER, 
    PHONESEARCHER, 
    EMAILSEARCHER, 
    USERSEARCHER
)


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