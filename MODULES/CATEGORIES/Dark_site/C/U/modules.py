#imports
import os
from time import sleep
from pathlib import Path
import subprocess
import sys

# Make the project package importable when this module is loaded directly.
project_root = Path(__file__).resolve().parents[5]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

#external calling imports
from MODULES.CATEGORIES.Dark_site.C.U.ascii import (
    MMK,
    GREEN
)

# Clear the terminal before showing the Money Maker menu.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#Loads The Money Maker Module
def MONEY_MAKER():
    clear_screen()

    #print the MMK Logo in Green
    print(f"{GREEN}{MMK}{GREEN}")
    print()

    #menu animation
    for dot in range(1, 5):
        print(f"\rPrepaire the Menu {'.' * dot}", end="", flush=True)
    sleep(1.5)

    #hop to mmk menu
    bad_men = Path(__file__).resolve().parent / "M" / "mmk.py"
    subprocess.run([sys.executable, str(bad_men)], check=False)