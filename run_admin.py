from file_manager import *
from admin_file_manager import *
from pathlib import Path
from Profile import Profile


def run_admin():

    while True:
        print("currently in admin mode.")
        while True:
            user_input = input()
            if user_input:
                command, *args = user_input.split()
                break
            else:
                print("no input")

        if command.lower() == 'q':
            break

        options = []
        if len(args) > 1:
            options = args
        if args:
            directory = Path(args[0])

        if command.lower() == 'l':
            try:
                if directory.is_dir():
                    list_directory(directory, options)
                else:
                    print('could not find directory.')
            except UnboundLocalError:
                print("please provide a directory")
                continue

        elif command.lower() == 'c':

            try:
                try:
                    while True:
                        print('Enter your username: ', end='')
                        username = str(input()).strip()
                        if ' ' in username:
                            print('Username cannot contain spaces')
                            continue

                        print('Enter your password: ', end='')
                        password = str(input()).strip()
                        if ' ' in password:
                            print('Password cannot contain spaces')
                            continue

                        break

                    print('Enter your bio: ', end='')
                    bio = str(input()).strip('\'"')

                except Exception:
                    print("could not make dsu file, please try again.")

                if (directory / (args[2] + '.dsu')).exists():
                    print("File already exists, opening file.")
                    journal = open_dsu_file(directory / (args[2] + '.dsu'))
                    journal.save_profile(directory / (args[2] + '.dsu'))
                    admin_mode(journal, (directory / (args[2] + '.dsu')))

                if not (directory / (args[2] + '.dsu')).exists():
                    dsu_path = create_file(directory, options)
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

        elif command.lower() == 'o':
            try:
                journal = open_dsu_file(directory)
                journal.save_profile(directory)
            except Exception as e:
                print(e)
                continue

            admin_mode(journal, directory)  # send to editor function

        else:
            print("invalid command")
            continue
