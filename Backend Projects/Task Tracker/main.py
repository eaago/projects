import json
import datetime
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=                    TASK TRACKER                    =")
        print("=                                                    =")
        print("======================================================")
        print("\nWelcome to your Personal Task Tracker!\nType 'help' for instructions.\n")

# Main
choice = ""
message = "What would you like to do?\n"

with open("task_list.json", "a+") as f:
    f.seek(0)

    try:
        task_list = json.load(f)
    except json.JSONDecodeError:
        task_list = []

clear_screen()

while True:
    print(message)
    choice = input("> task_cli ")

    token = choice.split(" ")

    if token[0] == "help" and len(token) == 1:
        message = """List of commands:
              \n`add`: Add a task to the tracker.\n\tUsage: add <task_name>
              \n`update`: Update the task name of an existing task.\n\tUsage: update <task_id> <new_name>
              \n`delete`: Delete an existing task.\n\tUsage: delete <task_id>
              \n`list`: List tasks. Can add extra parameter to sort based on progress.\n\tUsage: list <none|done|todo|in-progress>
              \n`mark-in-progress: Set task progress to in-progress.\n\tUsage: mark-in-progress <task_id>
              \n`mark-done`: Set task progress as done/completed.\n\tUsage: mark-done <task_id>`
              \n`help`: Prints this instruction list.\n\tUsage: help
              \n`close`: Closes and saves the tracker.\n\tUsage: close\n"""
        clear_screen()
    elif token[0] == "add":
        time = datetime.datetime.now()
        task_name = ""
        for i in range(len(token) - 1):
            print(i)
            if i != (len(token) - 2):
                task_name = task_name + token[i + 1] + " "
            else:
                task_name = task_name + token[i + 1]
        new_task = {
            "id": len(task_list) + 1,
            "description": task_name,
            "status": "todo",
            "createdAt": time.strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        task_list.append(new_task)
        print(new_task)
    elif token[0] == "update" and len(token) == 3:
        pass
    elif token[0] == "delete" and len(token) == 2:
        pass
    elif token[0] == "list":
        pass
    elif token[0] == "mark-in-progress":
        pass
    elif token[0] == "mark-done":
        pass
    elif token[0] == "close":
        print("\nTask Tracker closed. See you soon!")
        with open("task_list.json", "w") as f:
            json.dump(task_list, f, indent = 2)
        break
    else:
        message = "\nWrong input. Type 'help' for instructions.\n"
        clear_screen()