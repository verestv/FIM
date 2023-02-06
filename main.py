from colorama import Fore,Style
from newBL import *
from Monitoring import *
print(Style.BRIGHT + Fore.BLUE +"Welcome to File Integrity Monitor!"+ Style.RESET_ALL)

def start_menu():
    option = input("""What wuold you like to do?
                        A - Collect new Baseline 
                        B - Begin monitoring files with saved Baseline: """).upper()

    
    if option == 'A':
        newBaseline()
        print('Baseline succesfully renewed!')
    elif option == 'B':
        integrity_monitoring()
    else:
        print('Please enter an existing option(A/B)')
        start_menu()
start_menu()

    
        


