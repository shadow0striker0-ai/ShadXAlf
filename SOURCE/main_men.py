import re
import subprocess
from pathlib import Path
import unicodedata


def clear_screen():
    print("\033[2J\033[3J\033[H", end="", flush=True)


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
import subprocess
import sys

CYAN = '\033[96m'

print(f"{CYAN}{LOGO}{CYAN}")







def main():
    while True:
        raw_choice = input("Enter your choice: ")
        clean_choice = re.sub(r"\x1b\[[0-9;?]*[ -/]*[@-~]", "", raw_choice)
        normalized_choice = unicodedata.normalize("NFKC", clean_choice)
        choice = "".join(
            character for character in normalized_choice if character in "0123456789"
        )
        if not choice:
            continue
        if choice == "1":
            print("Username Searcher is coming soon!")
        elif choice == "2":
            print("Email Searcher is coming soon!")
        elif choice == "3":
            print("Phone Number Searcher is coming soon!")
        elif choice == "4":
            print("IP Tracker is coming soon!")
        elif choice == "5":
            print("Domain Searcher is coming soon!")
        elif choice == "6":
            print("Social Media Searcher is coming soon!")
        elif choice == "99":
            print("Exiting...")
            break
        elif choice == "999":
            credits_script = Path(__file__).resolve().parent / "MODULES" / "CREDITS" / "show_credits.py"
            subprocess.run([sys.executable, str(credits_script)], check=False)
            clear_screen()
            print(f"{CYAN}{LOGO}{CYAN}")
        else:
            print("Invalid choice. Please try again.")
main()