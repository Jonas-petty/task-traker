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
Should return a list with the tasks or a None if the file is empty
"""
def load_file(file_name):
    with open(file_name, "r+") as file:
        data = file.read()
        if data == "":
            return None
        return data

"""
Lists all the tasks saved on the file or informe that the file is empty
"""
def list_task():
    json_data = load_file("task-traker.json")
    if json_data != None:
        data = json.loads(json_data)
        print("Tasks:")
        for task in data:
            print(f"- {task["description"]}\tstatus: {task["status"]}")
    else:
        print("No Tasks available. Use the 'add' command to insert a new task.")
    


# TODO load the content of the file to add its content... it should be a different fucntion, so I could reuse it on the list argument.
def add(args):
    if len(args) == 3:
        with open("task-traker.json", "w+") as file:
            current_timestamp = datetime.now().strftime("%m/%d/%Y")
            task =  {
                "id": 1,
                "description": args[2],
                "status": "todo",
                "createdAt": current_timestamp,
                "updatedAt": current_timestamp
            }

            content = file.read()
            print(content)
            if content == "":
                tasks.append(task)
                json_tasks = json.dumps(tasks)
                file.write(json_tasks)
            else:
                json_tasks = json.loads(file)
                print(json)
            
            
        print(content)
        
    else:
        print('Please use two arguments to add a task (ex: python task-cli add "Task description")')


def handle_args(args):
    match args[1]:
        case "add":
            add(args)
        case "update":
            return args[1]
        case "delete":
            return args[1]
        case "mark-in-progress":
            return args[1]
        case "mark-done":
            return args[1]
        case "list":
            list_task()
        case "list-in-progress":
            return args[1]
        case _:
            return "Argument invalid"
        

     
handle_args(sys.argv)