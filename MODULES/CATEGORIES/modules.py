#imports
import os
from pathlib import Path
import subprocess
import sys
from time import sleep

#External module calls
from MODULES.UTILITIES.ascii import (
    COLORRESET, 
    COLOR_CHOICE, 
    IPTRACKER, 
    PHONESEARCHER, 
    EMAILSEARCHER, 
    USERSEARCHER,
    DOMAINSEARCHER
)

#loads the domain searcher module
def Domain_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the banner
    print(f"{COLOR_CHOICE}{DOMAINSEARCHER}{COLORRESET}")

    #Loads the tool Loading Animation
    for dot in range(1, 10):
        print(f"\rDomain Searcher is loading {'.' * dot}", end="", flush=True)
    sleep(0.5)

    #module path
    domain_module = (
        Path(__file__).resolve().parent
        / "Domain_search"
        / "Domain_methods.py"
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
    print(f"{COLOR_CHOICE}{IPTRACKER}{COLORRESET}") #Print the IP tracker logo

    #loading Animation
    for dot in range(1, 10):
        print(f"\rIP-Tracker is loading {'.' * dot}", end="", flush=True)
    sleep(0.5)
    print("Success")

#load the phone module
def Phone_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the phone number searcher logo
    print(f"{COLOR_CHOICE}{PHONESEARCHER}{COLORRESET}")

    #Loading animation
    for dot_count in range(1, 10):
        print(f"\rPhone-Searcher is loading {'.' * dot_count}", end="", flush=True)
    sleep(0.5)
    print("Success")

#load the email module
def email_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the email searcher logo
    print(f"{COLOR_CHOICE}{EMAILSEARCHER}{COLORRESET}")

    #Loading Animation
    for dot_count in range(1, 10):
        print(f"\rEmail Searcher is loading {'.' * dot_count}", end="", flush=True)
    sleep(0.5)
    print("Success")

#username function
def user_searcher():

    #clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #print the username searcher logo
    print(f"{COLOR_CHOICE}{USERSEARCHER}{COLORRESET}")

    #Loading Animation
    for dot_count in range(1, 10):
        print(f"\rUsername Searcher is loading {'.' * dot_count}", end="", flush=True)
    sleep(0.5)
    print("Success")