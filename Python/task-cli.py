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
    


J# TODO load the content of the file to add its content... it should be a different fucntion, so I could reuse it on the list argument.
def add(args):
    if len(args) == 3:
        with open("task-traker.json", "w+") as file:
            current_timestamp = datetime.now().strftime("%m/%d/%Y-%H:%M")
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
            return args[1]
        case "list-in-progress":
            return args[1]
        case _:
            return "Argument invalid"
        



        
handle_args(sys.argv)