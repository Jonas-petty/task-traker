import sys
from datetime import datetime
import json

task =  {
    "id": 0,
    "description": "",
    "status": "",
    "createdAt": "",
    "updatedAt": ""
}

tasks = []

"""
Returns a list with the tasks or None if the file is empty
"""
def load_file(file_name="task-traker.json"):
    try:
        with open(file_name, "+r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None


"""
Saves the data to the json file
"""
def save_file(data=[], file_name="task-traker.json"):
    try:
        with open(file_name, "w+") as file:
        
            data = json.dumps(data)
        
            file.writelines(data)
        return True
    except:
        return False


"""
Lists all the tasks saved on the file or inform that the file is empty
"""
def list_tasks():
    json_data = load_file()
    if json_data != None:
        data = json.loads(json_data)
        print("Tasks:")
        for task in data:
            print(f"{task["id"]} - {task["description"]}\tstatus: {task["status"]}")
    else:
        print("No Tasks available. Use the 'add' command to insert a new task.")


"""
Adds one or more tasks to the json file or creates it if the file does not exists
"""
def add_task(args):
    new_tasks = args[2:]
    if new_tasks:
        json_data = load_file()

        id = 1
        if json_data == None:
            data = []
        else:
            data = json.loads(json_data)
            id = len(data) + 1

        for task in new_tasks:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task =  {
                "id": id,
                "description": task,
                "status": "todo",
                "createdAt": current_date,
                "updatedAt": current_date
            }
            data.append(task)
            id += 1
        
        more_than_one = True if len(new_tasks) > 1 else False
        if save_file(data):
            print(f"{"Tasks" if more_than_one else "Task"} added successfully!")
        
    else:
        print("No task was informed, please try again.")
        

"""
Delete a task by its ID
"""
def delete_task(args):
    
    if len(args) == 3 and args[2].isdecimal() and int(args[2]) >= 1:
        id = int(args[2])
        json_data = load_file()
        data = json.loads(json_data)
        
        found = False
        for i, task in enumerate(data):
            if task["id"] == id:
                data.pop(i)
                save_file(data)
                found = True
                break

        if not found:
            print("Id is not available.")
    else:
        print("Wrong format, please try again.")


def handle_args(args):
    
    if len(args) <= 1:
        print("No argument informed")
    else:
        match args[1]:
            case "add":
                add_task(args)
            case "update":
                return args[1]
            case "delete":
                delete_task(args)
            case "mark-in-progress":
                return args[1]
            case "mark-done":
                return args[1]
            case "list":
                list_tasks()
            case "list-in-progress":
                return args[1]
            case _:
                print("Argument invalid")
         
handle_args(sys.argv)