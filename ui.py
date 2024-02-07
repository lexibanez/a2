# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lex Ibanez
# laibanez@uci.edu
# 70063614

# testpath
# C:\Users\lexib\OneDrive\Desktop\ICS32\a2tests

from file_manager import *
from pathlib import Path
from Profile import Profile # add Post when needed


def run_admin():

    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command.lower() == 'q':
            break

        options = []
        if len(args) > 1:
            options = args
        if args:
            directory = Path(args[0])

        if command.lower() == 'l':
            if directory.is_dir():
                list_directory(directory, options)
            else:
                print('Could not find directory.')

        elif command.lower() == 'c':

            try:
                
                try:
                    dsu_path = create_file(directory, options)

                    username = str(input('Enter your username: '))
                    password = str(input('Enter your password: '))
                    bio = str(input('Enter your bio: '))
                except Exception:
                    print("could not make dsu file, please try again.")

                else:
                    user_profile = Profile(username, password, bio)
                    user_profile.save_profile(dsu_path)
                    print("dsu file created and currently open")
                    edit_dsu_file(user_profile, dsu_path)
            except TypeError:
                print("could not make dsu file, please try again.")

            
            

        elif command.lower() == 'd':
            delete_file(directory)

        elif command.lower() == 'r':
            read_file(directory)
        
        elif command.lower() == 'o':
            open_dsu_file(directory)

        else:
            print("Invalid command.")
            continue

def run_user():
    pass


if __name__ == '__main__':
    run_admin()
