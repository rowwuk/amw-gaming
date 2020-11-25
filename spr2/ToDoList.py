#clear console on windows and unix
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else:
        _ = system('clear') 

#declare the table for the entire program
task_list = []

#task with name and done bool
class Task:
    def __init__(self, text, done):
        self.text = text
        self.done = done
      
#two display functions for easy use
def display_task(text, done):
    if done==True:
        print("[",i,"]", text, "- done!")
    else:
        print("[",i,"]", text)
    return

def display_list():
    print(" - - - To-Do Task List - - - \n")
    global i
    i=0
    while i != len(task_list):
        display_task(task_list[i].text, task_list[i].done)
        i+=1
    print("\n - - - ")
    return

#three main functions for task manipulation
def complete_task(x):
    if task_list[x].done == True:
        task_list[x].done = False
    else:
        task_list[x].done = True
    return

def pop_task(x):
    clear()
    print("\n Are you sure you want to delete [", x, "]", task_list[x].text,"? (y/n)") 
    y = input("\n ")
    if y == "yes" or y == "Yes" or y == "y":
        task_list.pop(x)
    return

def rename_task(x):
    clear()
    print("\n Enter a new name for [", x, "]", task_list[x].text,":") 
    y = input("\n ")
    task_list[x].text = y
    return

#sample tasks
task_list.append(Task("Sample Task 1", False))
task_list.append(Task("Sample Task 2", False))
task_list.append(Task("Sample Task 3", True))

#the main menu loop
while 1!=0:

    display_list()

    print("\n Available operations:")
    print("[1] Add a task to the list")
    print("[2] Mark task as completed")
    print("[3] Edit task name")
    print("[4] Expunge task")
    print("[5] Exit")

    choice = input("\n Select an operation: ")

    if choice == '1':
        clear()
        display_list()

        usr_input = input("\n Enter the name of the task: ")
        task_list.append(Task(usr_input, False))
        clear()

    elif choice == '2':
        clear()
        display_list()

        choice = input("\n Select a task to mark as done: ")
        complete_task(int(choice))
        clear()

    elif choice == '3':
        clear()
        display_list()

        choice = input("\n Select a task to rename: ")
        rename_task(int(choice))
        clear()

    elif choice == '4':
        clear()
        display_list()

        choice = input("\n Select a task to delete: ")
        pop_task(int(choice))
        clear()

    elif choice == '5':
        break
    else:
        clear()
        print("\n Invalid operation! \n")
        