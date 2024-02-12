# Lex Ibanez
# laibanez@uci.edu
# 70063614

# testpath
# C:\Users\lexib\OneDrive\Desktop\ICS32\a2tests

from file_manager import *
from pathlib import Path
from Profile import Profile


def run_admin():

    while True:
        while True:
            user_input = input()
            if user_input:
                command, *args = user_input.split()
                break
            else:
                print("ERROR")

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
                    username = str(input('Enter your username: '))
                    password = str(input('Enter your password: '))
                    bio = str(input('Enter your bio: '))

                    dsu_path = create_file(directory, options)
                except Exception:
                    print("could not make dsu file, please try again.")

                else:
                    journal = Profile(username, password, bio)
                    journal.save_profile(dsu_path)
                    print("dsu file created and currently open")
                    admin_mode(journal, dsu_path)
            except TypeError:
                print("could not make dsu file, please try again.")

            
        elif command.lower() == 'd':
            delete_file(directory)

        elif command.lower() == 'r':
            read_file(directory)
        
        elif command.lower() == 'o': ##TODO FIX ADMIN MODE
            try:
                journal = open_dsu_file(directory)
                journal.save_profile(directory)
            except Exception:
                print("ERROR")
                continue

            admin_mode(journal, directory) # send to editor function

        else:
            print("ERROR")
            continue


edit_menu_options_list = ['-usr', '-pwd', '-bio', '-addpost', '-delpost']
print_menu_options_list = ['-usr', '-pwd', '-bio', '-posts', '-post', '-all']

def run_ui(option):

    quit_flag = False

    while True:
        if quit_flag:
            return

        if option.lower() == 'c':
            directory = Path(input("Enter the directory where you would like to create the file: "))

            if directory.is_dir():
                try:
                    username = str(input('Enter your username: '))
                    password = str(input('Enter your password: '))
                    bio = str(input('Enter your bio: '))
                    file_name = str(input('Enter a name for the DSU file: '))
                        
                except Exception:
                    print("Could not make dsu file, please try again.")
                    break
                
                if not (directory / (file_name + '.dsu')).exists(): # if the file does not exist, create it
                    dsu_path = create_file(directory, ['-n', file_name])
                    journal = Profile(username, password, bio)
                    journal.save_profile(dsu_path)
                    print("Dsu file created and currently open")

                elif (directory / (file_name + '.dsu')).exists(): # if the file exists, open it
                        print("File already exists, opening file.")
                        journal = open_dsu_file(directory / (file_name + '.dsu'))
                        journal.save_profile(directory / (file_name + '.dsu'))

                while True:
                    print(f"\nCurrently looking at {file_name}.dsu, please enter a journal command, or 'Q' to close journal")
                    journal_menu_options()
                    command = input("Enter command: ").lower()
                    while command not in ["e", "p", "q"]:
                        print("Invalid command, please try again.")
                        journal_menu_options()
                        command = input("Enter command: ").lower()
                    
                    args = []
                    
                    if command == "e":
                        print(f"\nYou are now editing {file_name}.dsu, please enter an editing command")
                        edit_menu_options()
                        option = input("Enter a command: ")
                        while option not in edit_menu_options_list:
                            print("Invalid command, please try again.")
                            edit_menu_options()
                            option = input("Enter a command: ")
                        args.append(option)
                        option_input = handle_edit_options(option, journal)
                        print("Changes Saved")
                        args.append(option_input)
                    
                    elif command == "p":
                        print(f"\nYou are now looking at {file_name}.dsu, please enter an print command")
                        print_menu_options()
                        option = input("Enter a command: ")
                        while option not in print_menu_options_list:
                            print("Invalid command, please try again.")
                            edit_menu_options()
                            option = input("Enter a command: ")
                        args.append(option)
                        option_input = handle_print_options(option, journal)
                        args.append(option_input)

                        
                    if command == 'q':
                        quit_flag = True
                        break
                    
                    edit_dsu_file(journal, dsu_path, command, args)
            else:
                print("Could not find the specified directory, please try again.")

        elif option.lower() == 'o':
            while True:
                try:
                    directory = Path(input("Please enter the directory of the file you want to open: "))
                    journal = open_dsu_file(directory)
                    journal.save_profile(directory)
                    break
                except Exception:
                    print("Could not find the specified directory, or the path provided is not a .dsu file.\nPlease try again.")

            while True:
                print(f"\nCurrently looking at {directory.name}, please enter a journal command, or 'Q' to close journal")
                journal_menu_options()
                command = input("Enter command: ").lower()
                while command not in ["e", "p", "q"]:
                    print("Invalid command, please try again.")
                    journal_menu_options()
                    command = input("Enter command: ").lower()
                
                args = []
                
                if command == "e":
                    print(f"\n\nYou are now editing {directory.name}, please enter an editing command")
                    edit_menu_options()
                    option = input("Enter a command: ")
                    while option not in edit_menu_options_list:
                        print("Invalid command, please try again.")
                        edit_menu_options()
                        option = input("Enter a command: ")
                    args.append(option)
                    option_input = handle_edit_options(option, journal)
                    print("Changes Saved")
                    args.append(option_input)
                
                elif command == "p":
                    print(f"You are now looking at {directory.name}, please enter an print command")
                    print_menu_options()
                    option = input("Enter a command: ")
                    while option not in print_menu_options_list:
                        print("Invalid command, please try again.")
                        edit_menu_options()
                        option = input("Enter a command: ")
                    args.append(option)
                    option_input = handle_print_options(option, journal)
                    args.append(option_input)
                
                if command.lower() == 'q':
                    quit_flag = True
                    break 
                
                edit_dsu_file(journal, directory, command, args)
        

def journal_menu_options():
    print("-------------------------------------")
    print("E: Edit the current file")
    print("P: Print contents of the current file")
    print("Q: Quit editing menu")
    print("-------------------------------------")

def edit_menu_options():
    print("-------------------------------------")
    print("-usr: change your username")
    print("-pwd: change your password")
    print("-bio: change your bio")
    print("-addpost: make a post")
    print("-delpost: delete a post")
    print("-------------------------------------")

def print_menu_options():
    print("-------------------------------------")
    print("-usr: display your username")
    print("-pwd: display your password")
    print("-bio: display your bio")
    print("-posts: display all of your posts")
    print("-post: display a certain post")
    print("-all: display your whole profile")
    print("-------------------------------------")

def handle_edit_options(option, journal):
    if option == '-usr':
        return input("Enter your new username: ")
    if option == '-pwd':
        return input("Enter your new password: ")
    if option == '-bio':
        return input("Enter your new bio: ")
    if option == '-addpost':
        return input("Enter a post: ")
    if option == '-delpost':
        get_all_posts(journal)
        id = input("Enter the id of the post you would like to delete: ")
        return id

def handle_print_options(option,journal):
    if option == '-usr':
        return
    if option == '-pwd':
        return
    if option == '-bio':
        return
    if option == '-posts':
        return
    if option == '-post':
        get_post_indexes_only(journal)
        id = input("Enter the id of the post you would like to view: ")
        return id
    if option == '-all':
        return


def get_all_posts(journal):
    posts = journal.get_posts()
    i = 0
    for post in posts:
        print(f'{i}: {post["entry"]}')
        i += 1

def get_post_indexes_only(journal):
    posts = journal.get_posts()
    i = 0
    for post in posts:
        print(f'{i}:')
        i += 1