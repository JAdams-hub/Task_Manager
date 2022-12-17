# Task_Manager

## Overview
Program designed to work within cooperatively between teams, that aids in the management of tasks assigned to members of a team. 
Works with external data sources to create manipulate and store information regarding the users of the program and the details of tasks that are assigned to users. 
The program is capable of outputting statistics to external files and provides users with an efficient tool to manage their responsibilities.

## Installation
Open your terminal or command prompt

### Initializing the repository
1) Use 'cd' to change your directory then add/type your directory to initialize the directory of which you will place the local repository.
2) Use the command 'git init'

### Cloning the finalCapstone repository:
1) Enter 'git clone https://github.com/JAdams-hub/Task_Manager'

## Using the program
This program provides the user with the menu that essentially gives the user the ability to perform everything stated on the menu.

### Menu
The menu comes in the following format:

Select one of the following options below:
r - Registering a user
a - Add a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit

- Note that this menu is specifically for the admin of the program. Other users will not have access to the 'generate reports' and 'Display statistics' options.

### Files
tasks.txt - This file will hold a list of tasks, of which each task will have its own seperate line. The program will be able to read this file and output the tasks to the users in the program.

users.txt - This file will hold a list of the registered user's login details, of which each user will have its own line. Each line will start with the username followed by a comma and the password for the user.
The admin will be able to register new users for the program.
