import os
while True:
    command = input()
    if command == "End":
        break
    actions = command.split("-")
    action, file_name = actions[0], actions[1]

    if action == "Create":
        open(f"{file_name}", "w").close()
    elif action == "Add":
        with open(f"{file_name}", "a") as file:
            file.writelines(f"{actions[2]}\n")
    elif action == "Replace":
        if os.path.exists(f"{file_name}"):
            with open(f"{file_name}", "r+") as file:
                new_content = file.read().replace(actions[2], actions[3])
                file.seek(0)
                file.truncate()
                file.writelines(new_content)
        else:
            print("An error occurred")
    elif action == "Delete":
        if os.path.exists(f"{file_name}"):
            os.remove(f"{file_name}")
        else:
            print("An error occurred")
