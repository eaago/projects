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

def list_task(status):
    to_list = ""
    if status == "done":
        for task in task_list:
            if task["status"] == "done":
                to_print = f"[{task["id"]}]. {task["description"]}\n\tStatus: {task["status"]}\n\tCreated At: {task["createdAt"]}\n\tUpdated At: {task["updatedAt"]}\n"
                to_list = to_list + to_print
        if to_list == "":
            message = "No tasks marked as done.\n"
        else:
            message = to_list
        return message
    elif status == "todo":
        for task in task_list:
            if task["status"] == "todo":
                to_print = f"[{task["id"]}]. {task["description"]}\n\tStatus: {task["status"]}\n\tCreated At: {task["createdAt"]}\n\tUpdated At: {task["updatedAt"]}\n"
                to_list = to_list + to_print
        if to_list == "":
            message = "No tasks marked as todo.\n"
        else:
            message = to_list
        return message
    elif status == "in-progress":
        for task in task_list:
            if task["status"] == "in-progress":
                to_print = f"[{task["id"]}]. {task["description"]}\n\tStatus: {task["status"]}\n\tCreated At: {task["createdAt"]}\n\tUpdated At: {task["updatedAt"]}\n"
                to_list = to_list + to_print
        if to_list == "":
            message = "No tasks marked as in-progress.\n"
        else:
            message = to_list
        return message
    elif status == "all":
        to_list = ""
        for task in task_list:
            to_print = f"[{task["id"]}]. {task["description"]}\n\tStatus: {task["status"]}\n\tCreated At: {task["createdAt"]}\n\tUpdated At: {task["updatedAt"]}\n"
            to_list = to_list + to_print
        message = to_list
        return message
    
# Main
message = "What would you like to do today?\n"

with open("task_list.json", "a+") as f:
    f.seek(0)

    try:
        task_list = json.load(f)
    except json.JSONDecodeError:
        task_list = []

clear_screen()

while True:
    choice = ""

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
        message = f"Task \"{new_task["description"]}\" has been added.\n"
        clear_screen()
        
    elif token[0] == "update" and len(token) == 3:
        pass
    elif token[0] == "delete" and len(token) == 2:
        pass
    elif token[0] == "list":
        if len(token) == 1:
            message = list_task("all")
            clear_screen()
        elif len(token) == 2:
            if token[1] == "done":
                message = list_task("done")
                clear_screen()
            elif token[1] == "todo":
                message = list_task("todo")
                clear_screen()
            elif token[1] == "in-progress":
                message = list_task("in-progress")
                clear_screen()
            else:
                message = "Invalid parameters for 'list' command. Type 'help' for proper usage.\n"
                clear_screen()
        elif len(token) > 2:
            message = "Invalid parameters for 'list' command. Type 'help' for proper usage.\n"
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