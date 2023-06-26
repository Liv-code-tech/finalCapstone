import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# class Task_Manager is established

    # load_files: loads files to get program started

    # user_logins: logs users in and store user login info 

    # users, tasks and task subcategories are counted to be displayed or used to calculate stats displayed via generate_reports and display_stats:
        # tasks_per_user: counts number of tasks each user has by iterating through task_list and storing in dictionary
        # count_uswer_completed_tasks: counts number of completed tasks per user by iterating through task_list and storing in dictionary
        # count_user_overdue_tasks: counts number of overdue tasks per user by iterating through task_list and storing in dictionary
        # count_tasks: counts total number of stored tasks by iterating through task txt file and storing as variable
        # count_users: counts total number of stored users by iterating through user txt file and storing as variable
        # count_completed_tasks: counts total number of completed tasks by iterating through task_list and storing as variable
        # count_uncompleted_tasks: counts total number of incomplete tasks by iterating through task_list and storing as variable
        # count_overdue_tasks: counts total number of overdue tasks by iterating through task_list and storing as variable

    # stats for generate_reports section are calculated below:
        # percentage_of_tasks_per_user: calculates percentage share of tasks held by each user and store as dictionary
        # percentage_incomplete_tasks: calculates percentage of total tasks which are incomplete  
        # percentage_overdue: calculates percentage of total tasks which are overdue
        # percentage_user_complete_tasks: for each user, calculates percentage of tasks which are completed and store as dictionary
        # percentage_user_incomplete_tasks:  for each user, calculates percentage of tasks which are incomplete and store as dictionary
        # percentage_user_overdue_tasks: for each user, calculates percentage of tasks which are overdue and store as dictionary

    # show_menu: displays option menu with the below options to user and calls the relevant function based on their input:
        # reg_user: allows user to register a new user and add to user txt file
        # add_task: allows user to add new task and load to task txt file
        # view_all: displays all tasks, read from task txt file through task_list variable
        # view_mine: allows user to see their own tasks, read from task txt file through task_list variable
        # generate_reports: generates Task Overview and User Overview reports, formatted and read from txt files
        # display_stats: generates number of users and tasks



class Task_Manager():
    
    def __init__(self):
        self.today = datetime.today()
        self.task_data = []
        self.task_username = ""
        self.task_title = ""
        self.task_description = ""
        self.due_date_time = ""
        self.assigned_date = ""
        self.completed = False
        self.task_list = []
        self.user_list = []
        self.curr_user = ""
        self.user_overview_list = []
        self.count_user_overdue_tasks_dict = {}

    def load_files(self):
        # Open/create text files- one to store task data, one to store user login info
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as default_file:
                pass
        
        with open("tasks.txt", 'r') as task_file:
            self.task_data = task_file.read().split("\n")
            self.task_data = [t for t in self.task_data if t != ""]
        if not os.path.exists("user.txt"):
            with open("user.txt", "w") as default_file:
                # Load default user login
                default_file.write("admin;password")
        else:
            with open("user.txt", "r") as default_file:
                pass

        # Load empty list to store task info and count total number of tasks
        self.task_list = []
        self.task_total = 0

        # For every line in task file, task_total += 1 and blank dictionary curr_t is called
        for t_str in self.task_data:
            self.task_total += 1
            curr_t = {}
        # curr_t is the dictionary which assigns a key to each piece of task information
            # Split by semicolon and manually add each component
            self.task_components = t_str.split(";")
            curr_t['username'] = self.task_components[0]
            curr_t['title'] = self.task_components[1]
            curr_t['description'] = self.task_components[2]
            curr_t['due_date'] = datetime.strptime(self.task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(self.task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if self.task_components[5] == "Yes" else False
            # Add curr_t dictionary to task_list
            self.task_list.append(curr_t)
    
    def user_logins(self):
            with open("user.txt", 'r') as user_file:
                user_data = user_file.read().split("\n")
                # Convert to a dictionary
                self.username_password = {}
                for user in user_data:
                    if user != "":
                        username, password = user.split(';')
                        self.username_password[username] = password

                # Prompt user to log in, with appropriate checks to notify user if incorrect username/password is entered
                logged_in = False
                while not logged_in:
                    print("LOGIN")
                    self.curr_user = input("Username: ")
                    curr_pass = input("Password: ")
                    if self.curr_user not in self.username_password.keys():
                        print("User does not exist")
                        continue
                    elif self.username_password[self.curr_user] != curr_pass:
                        print("Wrong password")
                        continue
                    else:
                        print("Login Successful!")
                        logged_in = True
 
    def tasks_per_user(self):
        self.user_dict = {}
        for counter, task in enumerate(self.task_list):
            if self.user_dict.get(self.task_list[counter]['username']):
                self.user_dict[self.task_list[counter]['username']] = self.user_dict[self.task_list[counter]['username']] + 1
            else:
                self.user_dict[self.task_list[counter]['username']] = 1
        
        return self.user_dict

    def count_user_completed_tasks(self):
            self.user_dict_completed_tasks = {}
            for counter, task in enumerate(self.task_list):
                if self.user_dict_completed_tasks.get(self.task_list[counter]['username']):
                    if self.task_list[counter]['completed'] == True:
                        self.user_dict_completed_tasks[self.task_list[counter]['username']] += 1
                else:
                    if self.task_list[counter]['completed'] == True:
                        self.user_dict_completed_tasks[self.task_list[counter]['username']] = 1
                    else:
                        self.user_dict_completed_tasks[self.task_list[counter]['username']] = 0
            return self.user_dict_completed_tasks
   
    def count_user_overdue_tasks(self):
            self.count_user_overdue_tasks_dict = {}
            for counter, task in enumerate(self.task_list):
                if self.count_user_overdue_tasks_dict.get(self.task_list[counter]['username']):
                    if (self.task_list[counter]['completed'] == False) and (self.task_list[counter]['due_date'] < self.today):
                        self.count_user_overdue_tasks_dict[self.task_list[counter]['username']] += 1
                else:
                    if (self.task_list[counter]['completed'] == False) and (self.task_list[counter]['due_date'] < self.today):
                        self.count_user_overdue_tasks_dict[self.task_list[counter]['username']] = 1
                    else:
                        self.count_user_overdue_tasks_dict[self.task_list[counter]['username']] = 0
            return self.count_user_overdue_tasks_dict            
   
    def count_tasks(self):
        with open("tasks.txt", 'r') as task_file:
            self.total_task_number = 0
            for task in task_file: 
                self.total_task_number += 1
        return self.total_task_number

    def count_users(self):
        with open("user.txt", 'r') as user_file:
            self.total_user_number = 0
            for user in user_file: 
                self.total_user_number += 1
        return self.total_user_number

    def count_completed_tasks(self):
            complete_tasks = 0
            for counter, each_task in enumerate(self.task_list):
                if self.task_list[counter]['completed'] == True:
                    complete_tasks += 1
                else:
                    complete_tasks += 0
            return complete_tasks

    def count_uncompleted_tasks(self):
            incomplete_tasks = 0
            for counter, each_task in enumerate(self.task_list):
                if self.task_list[counter]['completed'] == False:
                    incomplete_tasks += 1
                else:
                    incomplete_tasks += 0
            return incomplete_tasks

    def count_overdue_tasks(self):
        complete_tasks = 0
        for counter, each_task in enumerate(self.task_list):
            if self.task_list[counter]['completed'] == False:
                if self.task_list[counter]['due_date'] < self.today:
                    complete_tasks += 1
            else:
                complete_tasks += 0
        return complete_tasks

    def percentage_of_tasks_per_user(self):
        percent_tasks_per_user = {}
        for user, value in self.user_dict.items():
            percent_tasks_per_user[user] = format((value / self.total_task_number) * 100, ".2f") + " %"
        return percent_tasks_per_user 

    def percentage_incomplete_tasks(self):
        result = format((self.count_uncompleted_tasks() / self.count_tasks()) * 100, ".2f") 
        return f"{result} %"

    def percentage_overdue(self):
        result = format((self.count_overdue_tasks() / self.count_tasks()) * 100, ".2f")
        return f"{result} %" 

    def percentage_user_complete_tasks(self):
        percent_complete_task_dict = {}
        for user, complete_tasks in self.user_dict_completed_tasks.items():
           percent_complete_task_dict[user] =  f"{round((complete_tasks / self.user_dict[user]) * 100, 2)} %"
        return percent_complete_task_dict

    def percentage_user_incomplete_tasks(self):
        percent_incomplete_task_dict = {}
        for user, complete_tasks in self.user_dict_completed_tasks.items():
            percent_incomplete_task_dict[user] = f"{round(100 - ((complete_tasks / self.user_dict[user]) * 100), 2)} %"
        return percent_incomplete_task_dict  

    def percentage_user_overdue_tasks(self):
        percentage_user_overdue_tasks_dict = {}
        for user, overdue_tasks in self.count_user_overdue_tasks_dict.items():
            percentage_user_overdue_tasks_dict[user] = f"{round((overdue_tasks / self.user_dict[user]) * 100, 2)} %"
        return percentage_user_overdue_tasks_dict

    def update_task_file(self):
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in self.task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

    def display_task(self, task_info, task_number):
        disp_str = f"""
Task Details: ID {task_number + 1}      

""" 
        disp_str += f"Task: \t\t\t {task_info['title']}\n"
        disp_str += f"Assigned to: \t\t {task_info['username']}\n"
        disp_str += f"Date Assigned: \t\t {task_info['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {task_info['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \t {task_info['description']}\n"
        disp_str += f"-------------------------------------------------------------------------"
        print(disp_str)

    def show_menu(self):
        while True:
            # presenting the menu to the user and
            # making sure that the user input is converted to lower case.
            print()
            menu = input('''Select one of the following Options below:
        r - registering a user
        a - adding a task
        va - view all tasks
        vm - view my task
        gr - generate reports
        ds - display statistics
        e - exit
        : ''').lower()

            if menu == 'r':
                self.reg_user()
            elif menu == 'a':
                self.add_task()
            elif menu == 'va':
                self.view_all()
            elif menu == 'vm':
                self.view_mine()
            elif menu == 'gr':
                self.generate_reports()
            elif menu == 'ds' and self.curr_user == 'admin':
                self.display_stats()
            elif menu == 'e':
                print('Goodbye!!!')
                exit()

    def reg_user(self):
            while True:
                # Request input of a new username
                # if username already exists:
                # Notify user and request reentry
                # else:
                # Request password and password confirmation
                new_username = input("New Username: ")
                if new_username in self.username_password.keys():
                    print("This username already exists. ")
                    continue
                else:
                    # Request input of a new password
                    new_password = input("New Password: ")
                    # Request input of password confirmation
                    confirm_password = input("Confirm Password: ")
                    # Check if the new password and confirmed password are the same
                    if new_password == confirm_password:
                        # If they are the same, add them to the user.txt file
                        self.username_password[new_username] = new_password
                        with open("user.txt", "a") as logins:
                            logins.write(f"\n{new_username};{new_password}")
                            print("New user added")
                            break
                    else:
                        print("Your passwords do not match. ")
                        continue

    def add_task(self):
        #     Prompt a user for the following:
        #      - A username of the person whom the task is assigned to
        #      - A title of a task
        #      - A description of the task and
        #      - The due date of the task
        self.task_username = input("Name of person assigned to task: ")
        if self.task_username not in self.username_password.keys():
            print("User does not exist. Please enter a valid username")
            self.task_username = input("Name of person assigned to task: ")
        elif self.task_username in self.username_password.keys():
            self.task_title = input("Title of Task: ")
            self.task_description = input("Description of Task: ")

        while True:
            try:
                self.task_due_date = input("Due date of task (YYYY-MM-DD): ")
                self.due_date_time = datetime.strptime(self.task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        #''' Add the data to the file task.txt and
        #    Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": self.task_username,
            "title": self.task_title,
            "description": self.task_description,
            "due_date": self.due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        self.task_list.append(new_task)
        self.update_task_file()
        print("Task successfully added.")
        self.count_user_completed_tasks()

    def view_all(self):
        for task_number in range(len(self.task_list)):
            task_info = self.task_list[task_number]
            self.display_task(task_info, task_number)

    def view_mine(self):
        my_task_list = []
        #for t in task_list:
        for task_number in range(len(self.task_list)):
            task_info = self.task_list[task_number]
            if task_info['username'] == self.curr_user:
                self.display_task(task_info, task_number)

        # Allows user to select a task to edit and alter it
        while True:
            edit_user_task = int(input("""To make changes to a task, please select task number,
    otherwise input '-1' to return to the main menu: """))
            if edit_user_task == -1:
                print(("\nYou have chosen to return to the main menu."))
                break
            elif self.task_list[edit_user_task-1]['completed'] == "Yes":
                print("\nYou cannot edit a completed task. ")
                break
            elif edit_user_task:
                print("Current Task Holder: " + self.task_list[edit_user_task-1]['username'])
                self.task_list[edit_user_task-1]['username'] = input("Change task holder: ")
                print(f"Current Due Date: {self.task_list[edit_user_task-1]['due_date']}")
                new_task_time = input("Change due date (YYYY-MM-DD): ")
                new_task_formatted = datetime.strptime(new_task_time, "%Y-%m-%d")
                self.task_list[edit_user_task-1]['due_date'] = new_task_formatted
                self.task_list[edit_user_task-1]['completed'] = input("Task complete? Please enter 'Yes' or 'No'. ")
                self.update_task_file()
                continue
            elif ValueError:
                pass

    def generate_reports(self):
        # Creates task_overview.txt and user_overview.txt if they do not exist
        if not os.path.exists("task_overview.txt"):
            with open("task_overview.txt", "x") as task_overview:
                pass
        if not os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "x") as user_overview:
                pass
        
        # Formats Task Overview and writes to task_overview.txt
        task_report = f"""
        -------------------------------------------------------------------------
            Task Overview  
        
            Number of Tasks: {self.count_tasks()}
            Completed Tasks: {self.count_completed_tasks()}
            Uncompleted Tasks: {self.count_uncompleted_tasks()}
            Overdue Tasks: {self.count_overdue_tasks()}
            Percentage of Incomplete Tasks: {self.percentage_incomplete_tasks()}
            Percentage of Tasks Overdue: {self.percentage_overdue()}
        -------------------------------------------------------------------------
            """
        with open("task_overview.txt", "w") as task_overview:
            task_overview.write(task_report)

        # Formats User Overview and writes to user_overview.txt
        user_report = f"""
        -------------------------------------------------------------------------
            User Overview
            
            Number of Users: {self.count_users()}
            Number of Tasks: {self.count_tasks()}
            Tasks per User: {self.tasks_per_user()} 
            Task share: {self.percentage_of_tasks_per_user()}
            Proportion of Completed Tasks: {self.percentage_user_complete_tasks()}
            Proportion of Incomplete Tasks:  {self.percentage_user_incomplete_tasks()}
            Proportion of Overdue Tasks for Each User: {self.percentage_user_overdue_tasks()}
        -------------------------------------------------------------------------"""
        with open("user_overview.txt", "w") as user_overview:
            user_overview.write(user_report)

        # Allows user to input request to read the Task or User Overview, or return to menu
        while True:
            report_type = input("""Select report:
            Enter 'to' to generate an overview of the tasks
            Enter 'uo' to generate an overview of the users
            To return to the main menu, enter '-1' """)
            if report_type == "to":
                with open("task_overview.txt", "r") as task_overview:
                    print(task_overview.read())
                break
            elif report_type == "uo":
                with open("user_overview.txt", "r") as user_overview:
                    print(user_overview.read())
                break
            elif report_type == "-1":
                print("\nYou have chosen to return to the main menu. ")
                break
            else:
                print("\nYou have not made a valid selection. ")
                continue

        pass

    def display_stats(self):
        num_users = len(self.username_password.keys())
        num_tasks = len(self.task_list)
        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")


myclass = Task_Manager()

myclass.load_files()
myclass.user_logins()
myclass.tasks_per_user()
myclass.count_user_completed_tasks()
myclass.count_user_overdue_tasks()
myclass.show_menu()

