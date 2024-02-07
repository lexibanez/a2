from pathlib import Path
from Profile import Profile
import json

def get_last_option(options):
    if len(options) == 3:
        return options[2]
    elif len(options) == 4:
        return options[3]


def list_directory(directory, options):
    contents = list(directory.iterdir())
    # sort contents for files
    files = [x for x in contents if x.is_file()]
    # sort contents for directories
    directories = [x for x in contents if x.is_dir()]

    if '-e' in options:
        suffix = get_last_option(options)

        for file in files:
            if file.suffix == '.' + suffix:
                print(file)
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    elif '-s' in options:
        search_file = get_last_option(options)

        # checks if the search file has a path
        if Path(directory / search_file).is_file():
            print(Path(directory / search_file))
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    elif '-f' in options:
        for file in files:
            print(file)
        for directory in directories:
            if '-r' in options:
                list_directory(directory, options)

    else:
        for file in files:
            print(file)
        for directory in directories:
            print(directory)
            if '-r' in options:
                list_directory(directory, options)


def create_file(directory, options):
    if not directory.is_dir():
        print("not a directory")
        raise Exception("not a directory")
    
    if "-n" in options:
        index = options.index('-n')
        if index + 1 < len(options):
            file_name = options[index + 1]
            new_path = directory / f'{file_name}.dsu'
            new_path.touch()
        else:
            print("missing file name")
            raise Exception("missing file name")
    else:
        print("missing -n option")
        raise Exception("missing -n option")
    
    return new_path


def delete_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            file_name = directory
            directory.unlink()
            print(f'{file_name} DELETED')
        else:
            print("ERROR")
    else:
        print("ERROR")


def read_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            with open(directory, 'r') as file:
                content = file.read()
                if not content:
                    print("empty file")
                else:
                    print(content.strip())
        else:
            print("not a dsu file")
    else:
        print("not a file")

def open_dsu_file(directory):
    if directory.is_file():
        if directory.suffix == '.dsu':
            print("file opened")
            user_profile = Profile() # instantiate a new profile object
            user_profile.load_profile(directory) # load the profile from the file system into the object
            edit_dsu_file(user_profile, directory) # send to editor function
        else:
            print("not a .dsu file")
    else:
        print("could not open the file")
    

def edit_dsu_file(user_profile: Profile, dsu_path: str):

    while True:
        print("currently editing opened file, please enter an editing command, or Q to quit editing")
        user_input = input("Enter a profile editing command: ")
        command, *args = user_input.split()

        if command.lower() == 'q':
            break
        
        elif command.lower() == 'e':
            if '-usr' in args:
                username = args[args.index('-usr') + 1]
                user_profile.username = username
                user_profile.save_profile(dsu_path)
            elif '-pwd' in args:
                pwd = args[args.index('-pwd') + 1]
                user_profile.password = pwd
                user_profile.save_profile(dsu_path)
            elif '-bio' in args:
                bio = args[args.index('-bio') + 1]
                user_profile.bio = bio
                user_profile.save_profile(dsu_path)
            elif '-addpost' in args:
                pass
            elif '-delpost' in args:
                pass