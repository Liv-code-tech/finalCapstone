### Final Capstone

﻿This programme is the end result of a refactoring assignment from my Software Engineering bootcamp, provided by HyperionDev and funded by the Department of Education. It is designed to serve as an employee task-management system for a small company. It allows employee details to be stored in one place, along with an up-to-date history of their working tasks and additional information which can be used to note trends in the allocation and completion of tasks. 


**_Summary of Code_**  
HyperionDev provided me with a piece of code with no functions or classes, which included functionality for formatting and loading information from tasks.txt and user.txt; display the options menu; allow the user to choose from the following:

Register a new user  
Add a task  
View all tasks  
View their own tasks  
Display statistics  
Exit

It had no classes or functions, no Generate Reports section and neither the task_overview.txt or the user_overview.txt file.

Text files are used to store employee/user login details and task information. The programme contains functionality which allows both of these text files to be altered; either when a new user or task is added, or when a task is modified. 


**_FUNCTIONALITY ADDED BY ME_**  
All functionality in the program was moved or written into functions.


My alterations to functions containing existing code:


**Register User (reg_user())**  
I modified the function reg_user() to ensure that usernames are not duplicated when added to user.txt and that an appropriate error message is shown, subsequently allowing the user to try entering another username.

**View Mine (view_mine())**  
I formatted the function view_mine() to display the user’s tasks in a readable way, along with a corresponding number which can be used to identify each task.
The ID number could then be used to select a specific task, or a user could enter ‘-1’ to return to the main menu. If the selected task is already marked as complete, the user receives a message saying that the task is complete and cannot be edited. Otherwise, if the user selects a task, they can mark it as complete, or change its affiliated user, due date and completion status.This renewed information alters the task information in tasks.txt.  



**_Functions I wrote from scratch:_**  
**Generate Reports (generate_reports())**  
I created a new function called generate_reports(). 
If you select the Display Statistics option on the menu, the programme will output the number of users and tasks which are stored in the programme’s main text files, tasks.txt and user.txt. 

Formatted sets of statistics are saved in text files task_overview.txt and user_overview.txt, to be displayed if you select the Generate Reports option on the menu, which will give you two choices:

**1. Task Overview**  
Number of tasks in the programme  
Number of tasks marked as complete  
Number of tasks marked as incomplete  
Number of overdue tasks  
Percentage of total tasks which are incomplete  
Percentage of total tasks which are overdue  

**2. User Overview**  
Number of users in the programme  
Number of tasks in the programme  
Number of tasks held by each user  
Percentage share of tasks held by each user  
Percentage of each user’s tasks which are complete  
Percentage of each user’s tasks which are incomplete  
Percentage of each user’s tasks which are overdue  

In order to produce these statistics, I created a number of additional functions, containing counters and formulas to calculate them.
