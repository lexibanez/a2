# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lex Ibanez
# laibanez@uci.edu
# 70063614

# a1.py

# Starter code for assignment 1 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lex Ibanez
# laibanez@uci.edu
# 70063614

from ui import run_admin

def main():
    admin = input("Are you an admin? (y/n): ")
    if admin.lower().strip() == 'y':
        run_admin()
    else:
        print('fuck off')



if __name__ == '__main__':
    main()