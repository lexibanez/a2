a2.py is a program that allows a user to create and modify
a dsu profile locally on their computer. Users can also 
open existing dsu profiles, and then continue editing them.

A dsu profile contains a username, password, bio, and posts
with timestamps. Each time a new dsu profile is created, the
user must create a username, password, and bio.

At program entry, the user make choose to create a file, open
a file, or quit the program. However, there is a hidden mode 
when you type admin at program entry. The program will then 
no longer have a user interface, and the command format is:

[COMMAND] [INPUT] [[-]OPTION] [INPUT]

Admin mode still retains all of the functionality from 
assignment 1. New features include the C command to create
a file, and O to open a file. The format for creating a file is:

C [directory] -n [name]

Once a file is created or opened. The user enters the edit menu.
The edit menu command format is:

[COMMAND] [OPTION] [INPUT]

There are 2 commands in the edit menu, edit (E), and print (P).
For edit, the options include -usr, -pwd, -bio, -addpost, and
-delpost. These options allow the user to edit the dsu profile 
directly. For print, the options include -usr, -pwd, -bio, -posts
-post, and -all. These options print out different contents of the
open dsu file.

If the user does not enter admin mode, then the user interface is active.
The create and open file functionalities are available in UI mode, but
there is no need for the strict input format as the UI guides the user.
UI mode however does not retain functionality from assignment 1.
