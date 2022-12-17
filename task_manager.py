# ====Function Section====

# Allows the user to register a new user and stores the user data into user.txt
# Asks user to confirm password, if they do not match the user is redirected to the menu.
# If username is taken/matches username in user.txt, user is prompted with message and function starts again.
def reg_user():
    new_username = input("\nEnter a new username: ")
    new_password = input("Enter a new password: ")
    confirm_password = input("Enter your password again: ")
    with open("user.txt", "r") as user_text:
        for line in user_text:
            split_user_text = line.split(", ")
            if split_user_text[0] == new_username:
                print("\nUsername already taken.")
                return reg_user()
    if confirm_password == new_password:
        with open("user.txt", "a") as user_list:
            user_list.write(f"\n{new_username}, {new_password}")
            user_list.write("".replace("\n", ""))
            print(f"New user '{new_username}' has been created.")
    else:
        print("\nThe passwords do not match. Redirecting to the menu...\n")

# User creates and inputs details of a new task to be added to tasks.txt.
# The task will be added to a new line on the file.
def add_task():
    print("\nWelcome to enter a new task.")
    task_user = input("\nEnter the username to assign this task to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    task_due_date = input("Enter the current date (dd/mm/yyyy): ")
    current_date = input("Enter the due date of the task (dd/mm/yyyy): ")
    print("\nTask added.")
    with open("tasks.txt", "a") as task_file:
        task_file.write(f"\n{task_user}, {task_title}, {task_description}, {task_due_date}, {current_date}, No")

# Outputs information of all the tasks stored within tasks.txt
# Displays appropriate message if task list is finished, or if there are no tasks in the task list.
def view_all():
    no_user_task_message = "No tasks available."
    end_of_list_message = "End of task list."
    print("\nWelcome to view all tasks.")
    with open("tasks.txt", "r") as read_task_file:
        task_counter = -1
        for line in read_task_file:
            task_list = line.split(", ")
            task_counter += 1
            print(f"\nTask {task_counter}\nUser:\t\t\t{task_list[0]}\nTask Title:\t\t{task_list[1]}"
                  f"\nDescription:\t{task_list[2]}\nDue Date:\t\t{task_list[3]}\nCurrent Date:\t{task_list[4]}"
                  f"\nCompleted?\t\t{task_list[5]}")
    if task_counter >= 1:
        no_user_task_message = ""
        print(no_user_task_message)
        print(end_of_list_message)
    elif task_counter < 0:
        end_of_list_message = ""
        print(end_of_list_message)
        print(no_user_task_message)

# Displays the tasks assigned to user.
# Displays appropriate message if user task list is finished, or there are no tasks assigned to user.
def view_mine():
    print(f"\n{logged_in_user}'s tasks:")
    with open("tasks.txt", "r") as read_task_file:
        task_counter = -1
        file_lines = []
        for line in read_task_file:
            file_lines.append(line.split(", "))
            task_list = line.split(", ")
            task_counter += 1
            if task_list[0] == logged_in_user:
                print(f"\nTask {task_counter}\nUser:\t\t\t{task_list[0]}\nTask Title:\t\t{task_list[1]}"
                      f"\nDescription:\t{task_list[2]}\nDue Date:\t\t{task_list[3]}\nCurrent Date:"
                      f"\t{task_list[4]}\nCompleted?\t\t{task_list[5]}")

        # User inputs the task they would like to edit or whether they would like to return to the menu.
        # Appropriate error messages are outputted if task doesn't exist, or if task isn't matched to logged_in_user.
        # User is unable to edit tasks already completed.
        if task_counter >= 0:
            choose_task = int(input("\n- Enter the task number to edit the task"
                                    "\n- Enter -1 to return to the main menu\n:"))
            if choose_task > task_counter:
                print("\nInvalid selection"
                      "\nReturning to menu...")
                return menu
            elif file_lines[choose_task][5] == "Yes\n" or file_lines[choose_task][5] == "Yes":
                print("\nYou can only edit files that are not complete."
                      "\nRedirecting to menu...")
                return menu
            elif choose_task == -1:
                return menu

            # User chooses an option that will either edit the task
            # or edit the 'No' value to 'Yes' for completed on the task
            vm_options = input("\nChoose an option:"
                               "\nmt - Mark task as complete"
                               "\net - Edit task"
                               "\n: ").lower()
            with open("tasks.txt", "r") as read_task_file:
                task_list_two = []
                for line in read_task_file:
                    task_list_two.append(line.split(", "))
                if task_list_two[choose_task][0] == logged_in_user:
                    if vm_options == "mt":
                        task_list_two[choose_task][5] = "Yes\n"
                        print("\nTask updated.")
                    elif vm_options == "et":
                        
                        # User inputs whether they want to edit the user that the task is assigned to
                        # or to edit the due date on the task
                        assignee_or_due_date = input("\nChoose an option:"
                                                     "\nea - Edit assignee"
                                                     "\ned - Edit due date"
                                                     "\n: ")
                        if assignee_or_due_date == "ea":
                            new_assignee = input("Enter the user to assign this task to: ")
                            task_list_two[choose_task][0] = new_assignee
                            print("\nTask updated.")
                        elif assignee_or_due_date == "ed":
                            new_due_date = input("Enter a new due date (dd/mm/yyyy): ")
                            task_list_two[choose_task][4] = new_due_date
                            print("\nTask updated.")
                        else:
                            print("Invalid option.")
                            return menu
                    else:
                        print("Invalid option.")
                        return menu
                elif task_list_two[choose_task][0] != logged_in_user:
                    print(f"\nYou are unable to edit this task. You can only edit tasks assigned to you.")
                elif task_list_two[choose_task][5] == "No\n":
                    print("You can only edit tasks that are not completed.")
                    return menu
                edited_list = ""
                for list in task_list_two:
                    edited_list = edited_list + ", ".join(list).replace("\n", "") + "\n"
                    with open("tasks.txt", "w") as updated_task_file:
                        updated_task_file.write(edited_list)

def generate_reports():

    # ===task_overview.txt report===
    generate_task_report = []
    completed_tasks = []
    uncompleted_tasks = []
    overdue_tasks = []
    # completed_tasks2 used for percentage of tasks assigned to user that is completed
    completed_tasks2 = []
    # uncompleted_tasks2 used for percentage of uncompleted tasks assigned to user
    uncompleted_tasks2 = []
    with open("tasks.txt", "r") as task_file:
        for line in task_file:
            generate_task_report.append(line.split(", "))
        # Appends the 'Yes'/completed tasks to the 'completed_tasks' list.
        for element in generate_task_report:
            if element[5] == "Yes" or element[5] == "Yes\n":
                completed_tasks.append(element[5])
                completed_tasks2.append(element)
            # Appends the number of 'no'/uncompleted tasks to the 'uncompleted_tasks' list.
            elif element[5] == "No" or element[5] == "No\n":
                uncompleted_tasks.append(element[5])
                uncompleted_tasks2.append(element)
                if element[4][-4::] <= element[3][-4::]:
                    if element[4][3:5] < element[3][3:5]:
                        overdue_tasks.append(element)
                    elif element[4][3:5] <= element[3][3:5] and element[4][0:2] < element[3][0:2]:
                        overdue_tasks.append(element)

        total_tasks = len(generate_task_report)
        total_completed = len(completed_tasks)
        total_uncompleted = len(uncompleted_tasks)
        total_overdue = len(overdue_tasks)

        with open("task_overview.txt", "w") as task_overview:
            task_overview.write(f"---Overview of tasks---"
                                f"\n\nTotal tasks:\t\t{str(total_tasks)}"
                                f"\nTotal completed:\t\t{str(total_completed)}"
                                f"\nTotal incomplete:\t\t{str(total_uncompleted)}"
                                f"\nTotal overdue:\t\t{total_overdue}"
                                f"\nIncomplete tasks:\t\t{round((total_uncompleted / total_tasks) * 100, 2)}%"
                                f"\nOverdue tasks:\t\t{round((total_overdue / total_tasks) * 100, 2)}")

        # ===user_overview.txt report===
        generate_users = []
        names = []
        task_assigned_names = []
        overdue_names = []
        completed_names = []
        uncompleted_names = []
        user_overview_str = ""
        with open("user.txt", "r") as user_file:
            for line in user_file:
                generate_users.append(line.split(", "))
            for name in generate_users:
                names.append(name[0])
            # Retrieving count of tasks per user
            for element2 in generate_task_report:
                task_assigned_names.append(element2[0])
            # Appends the assigned user of each overdue task to the list overdue_names
            for item in overdue_tasks:
                overdue_names.append(item[0])
            # Appends the assigned user of each completed task to list completed_names
            for completed in completed_tasks2:
                completed_names.append(completed[0])
            # Appends the assigned user of each incomplete task to list uncompleted_names
            for uncompleted in uncompleted_tasks2:
                uncompleted_names.append(uncompleted[0])

            # Outputs the information to user_overview.txt
            with open("user_overview.txt", "w") as user_overview:
                user_overview_str += f"---Overview of users---\n" \
                                        f"\nNumber of users:\t\t{len(names)}" \
                                        f"\nTotal number of tasks:\t{total_tasks}"

                for users in names:
                    user_overview_str += f"\n\n{users}'s overview: "
                    user_overview_str += f"\nTasks assigned:\t{task_assigned_names.count(users)}"
                    if total_tasks > 0:
                        user_overview_str += f"\n% of total tasks assigned:" \
                                            f"\t{round((task_assigned_names.count(users) /total_tasks)* 100, 2)}%"
                    elif total_tasks == 0:
                        user_overview_str += f"\n% of total tasks assigned:\t0%"

                    if len(completed_tasks2) > 0:
                        user_overview_str += f"\n% of total completed tasks:" \
                                    f"\t{round((completed_names.count(users) / len(completed_tasks2)) * 100, 2)}%"
                    elif len(completed_tasks2) == 0:
                        user_overview_str += f"\n% of total completed tasks:\t0%"

                    if len(uncompleted_tasks) > 0:
                        user_overview_str += f"\n% of total uncompleted tasks:" \
                                    f"\t{round((uncompleted_names.count(users) / len(uncompleted_tasks)) * 100, 2)}%"
                    elif len(uncompleted_tasks) == 0:
                        user_overview_str += f"\n% of total uncompleted tasks:\t0%"

                    if len(overdue_tasks) > 0:
                        user_overview_str += f"\n% of total overdue tasks:" \
                                            f"\t{round((overdue_names.count(users) / len(overdue_tasks)) * 100, 2)}%"
                    elif len(overdue_tasks) == 0:
                        user_overview_str += f"\n% of total overdue tasks:\t0%"
                user_overview.write(user_overview_str)


# ====Login Section====

# Allows the code to know if the user is logged in, whether their username is found in user.txt
# and who the logged-in user is.
user_logged_in = False
username_found = False
logged_in_user = ""

#  Error message contains specific message if username or password is incorrect
incorrect_username = "\nUsername not found\n"
incorrect_password = "\nIncorrect Password\n"
error_message = ""

# User inputs username and password, and if they match the user login info on user.txt then user will be logged in.
# If username or password do not match list of usernames and passwords in user.txt, error code is outputted.
while not user_logged_in:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    username_found = False
    with open("user.txt", "r") as user_text:
        for line in user_text:
            user_login_info = line.split(", ")
            listed_username = str(user_login_info[0])
            listed_password = str(user_login_info[1].replace("\n", ""))
            if username == listed_username:
                username_found = True
                if password == listed_password:
                    print(f"\nWelcome {username}!")
                    user_logged_in = True
                    logged_in_user = username
                else:
                    error_message = incorrect_password
            elif not username_found:
                error_message = incorrect_username
    if user_logged_in:
        error_message = ""
    print(error_message)

# ====Menu Section====

while user_logged_in:

    # Displays menu to the admin has access to 'Display statistics' option.
    # User input is converted to lowercase.
    if logged_in_user == "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Add a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

        # If the user is the admin, they are able to input the details of the new user.
        # Appropriate message is displayed if the user is not the admin.
        # Runs the function 'reg_user'.
        if menu == 'r' and logged_in_user == "admin":
            print("\nWelcome to register a new user.")
            reg_user()
        elif menu == 'r' and logged_in_user != "admin":
            print(f"\nOnly the admin has access to this feature. Sorry {logged_in_user}.")

        # Runs the function 'add_task'
        elif menu == 'a':
            add_task()

        # Outputs information of all the tasks stored within tasks.txt
        # Displays appropriate message if task list is finished, or if there are no tasks in the task list.
        elif menu == 'va':
            view_all()

        # Displays the tasks assigned to user.
        # Displays appropriate message if user task list is finished, or there are no tasks assigned to user.
        elif menu == 'vm':
            view_mine()

        # Generates reports task_overview.txt and user_overview.txt
        elif menu == 'gr' and logged_in_user == "admin":
            print("\nReports generated.\n")
            generate_reports()


        # Display Statistics - Displays number of users and number of tasks.
        elif menu == 'ds' and logged_in_user == "admin":
            print("\nWelcome to Display statistics\n")
            generate_reports()
            with open("task_overview.txt", "r") as task_overview:
                print(task_overview.read())
            #    for lines in task_overview:
            #        print(lines.replace("\n", ""))
            print("\n")
            with open("user_overview.txt", "r") as user_overview:
                print(user_overview.read())
            #    for lines2 in user_overview:
            #        print(lines2.replace("\n", ""))



        # Exits the menu and ends the program.
        elif menu == 'e':
            print('Goodbye!')
            exit()

        # Outputs message if user input is not on the menu.
        else:
            print("Selected choice not in menu, please try again.")

    # Displays menu to the user.
    # User input is converted to lowercase.
    elif logged_in_user != "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()


# If the user is the admin, they are able to input the details of the new user.
# Appropriate message is displayed if the user is not the admin.
# The details are then added and stored in user.txt as another user that can log in.
        if menu == 'r' and logged_in_user == "admin":
            print("\nWelcome to register a new user.")
            reg_user()
        elif menu == 'r' and logged_in_user != "admin":
            print(f"\nOnly the admin has access to this feature. Sorry {logged_in_user}.")

# Runs the function 'add_task'
        elif menu == 'a':
            add_task()

# Outputs information of all the tasks stored within tasks.txt
# Displays appropriate message if task list is finished, or if there are no tasks in the task list.
        elif menu == 'va':
            view_all()

# Displays the tasks assigned to user.
# Displays appropriate message if user task list is finished, or there are no tasks assigned to user.
        elif menu == 'vm':
            view_mine()

# Exits the menu and ends the program.
        elif menu == 'e':
            print('Goodbye!')
            exit()

# Outputs message if user input is not on the menu.
        else:
            print("Selected choice not in menu, please try again.")
