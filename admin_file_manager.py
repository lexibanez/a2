from file_manager import get_argument_value, get_all_posts, check_input, check_spaces
from Profile import Profile, Post

def admin_mode(journal: Profile, dsu_path: str):

    while True:
        while True:
            user_input = input().strip()
            if user_input:
                command, *args = user_input.split()
                break
            else:
                print("enter a dsu file")

        if command.lower() == 'q':
            break

        elif command.lower() == 'e':
            if '-usr' in args:
                username = get_argument_value(args, '-usr')
                status = check_input(username)
                if status == False:
                    continue
                journal.username = username
                journal.save_profile(dsu_path)
            if '-pwd' in args:
                pwd = get_argument_value(args, '-pwd')
                status = check_input(pwd)
                if status == False:
                    continue
                journal.password = pwd
                journal.save_profile(dsu_path)
            if '-bio' in args:
                bio = get_argument_value(args, '-bio')
                status = check_spaces(bio)
                if status == False:
                    continue
                journal.bio = bio
                journal.save_profile(dsu_path)
            if '-addpost' in args:
                post_content = get_argument_value(args, '-addpost')
                status = check_spaces(post_content)
                if status == False:
                    continue
                post = Post(post_content)
                journal.add_post(post)
                journal.save_profile(dsu_path)
            if '-delpost' in args:
                index = int(get_argument_value(args, '-delpost'))
                journal.del_post(index)
                journal.save_profile(dsu_path)

        elif command.lower() == 'p':
            if '-usr' in args:
                print(journal.username)
            if '-pwd' in args:
                print(journal.password)
            if '-bio' in args:
                print(journal.bio)
            if '-posts' in args:
                get_all_posts(journal)
            if '-post' in args:
                try:
                    id = get_argument_value(args, '-post')
                    if id:
                        print(journal.get_posts()[int(id)]["entry"])
                    else:
                        print("provide a number")
                except IndexError or ValueError:
                    print("index out of range")
                    continue
            if '-all' in args:
                print(journal.__str__())
                get_all_posts(journal)
        else:
            print("not a command")
