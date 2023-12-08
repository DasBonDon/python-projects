# A command-line to-do list.
import json

# Function to add a task to the list
def add_task():
    while True:
        task = input("\nWhat task would you like to add? ")
        if task.lower() not in tasks:
            tasks.append(task.lower())
        else:
            print("\nThat task already exists!")

        # Check if the user wants to add another task
        choice = input("\nWould you like to add another task? (Y/N) ")
        if choice.lower() != 'y':
            break

# Function to mark a task as completed
def mark_completed():
    task = input("\nWhat task would you like to mark as complete? ").lower()
    if task in tasks:
        print("\nThat task has been marked as completed!")
        completed.append(task)
        tasks.remove(task)
    else:
        print("\nThat task doesn't exist!")

# Function to display pending tasks
def view_pending():
    print("\nHere is your list of pending tasks!")
    for task in tasks:
        print(f"\n\t- {task.title()}")

# Function to remove a task
def remove_task():
    task = input("\nWhich task would you like to remove? ")
    if task.lower() in tasks:
        print("\nThat task has been removed!")
        tasks.remove(task)
    else:
        print("\nThat task doesn't exist!")

# Function to display completed tasks
def view_completed():
    print("\nHere is your list of completed tasks!")
    for task in completed:
        print(f"\n\t- {task.title()}")

# File names for storing tasks and completed tasks
tasks_file = "tasks.json"
completed_file = "completed.json"

# Loading tasks and completed tasks from JSON files if available
try:
    with open(tasks_file, 'r') as tasks_json:
        tasks = json.load(tasks_json)
except FileNotFoundError:
    tasks = []

try:
    with open(completed_file, 'r') as completed_json:
        completed = json.load(completed_json)
except FileNotFoundError:
    completed = []

# User interaction loop
while True:
    prompt = "\nWhat would you like to do?"
    prompt += ("\n1. Add a task"
               "\n2. Mark a task as complete"
               "\n3. View pending tasks"
               "\n4. Remove a task"
               "\n5. View completed tasks"
               "\n6. Close program"
               "\nChoose an option (1-6): ")

    answer = input(prompt)

    if answer == '1':
        add_task()
    elif answer == '2':
        mark_completed()
    elif answer == '3':
        view_pending()
    elif answer == '4':
        remove_task()
    elif answer == '5':
        view_completed()
    elif answer == '6':
        # Save tasks and completed tasks before exiting
        with open(tasks_file, 'w') as tasks_json:
            json.dump(tasks, tasks_json)
        with open(completed_file, 'w') as completed_json:
            json.dump(completed, completed_json)
        break
    else:
        print("\nInvalid option! Please choose a number between 1 and 6.")