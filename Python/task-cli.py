# Task Traker
import os
import sys
import json

tasks = []
task = {
    "id": 0,
    "description": "",
    "status": "",
    "created_at": "",
    "updated_at": ""
}


def main():
    if os.path.exists("task-traker.json"):
        with open("task-traker.json", "r+") as file:
            data = json.load(file)

            if isinstance(data, list):
                data.append(task)
                print(data)
            else:
                data = tasks.append(task)
            
            json.dump(data, file)

            file.truncate()
    else:
        with open("task-traker.json", "w+") as file:
            tasks.append(task)
            json.dump(tasks, file)



if __name__ == "__main__":
    main()