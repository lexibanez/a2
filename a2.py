# Lex Ibanez
# laibanez@uci.edu
# 70063614

# testpath
# C:\Users\lexib\OneDrive\Desktop\ICS32\a2tests

from ui import run_ui
from run_admin import run_admin


def main():
    while True:
        user_input = input("Welcome! Would you like to create or open a "
                           "DSU file? Enter C to create a file, O to "
                           "open a file, Q to quit: ")
        while user_input not in options:
            user_input = input("Invalid command, please enter C to create "
                               "a file, O to open a file, Q to quit: ")

        if user_input.lower().strip() == 'admin':
            run_admin()
        elif user_input.lower() == 'q':
            break
        else:
            run_ui(user_input)


options = ['admin', 'o', 'c', 'q']

if __name__ == '__main__':
    main()
