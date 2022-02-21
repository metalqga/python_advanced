import os


def list_dir(current_path, files_dict):
    for el in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, el)):
            list_dir(os.path.join(current_path, el), files_dict)
        else:
            extensions = el.split(".")[-1]
            if extensions not in files_dict:
                files_dict[extensions] = []
            files_dict[extensions].append(el)


type_of_files = {}
starting_folder = input()

list_dir(starting_folder, type_of_files)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

with open(os.path.join(desktop, 'report.txt'), "w") as f:
    for extension, files in sorted(type_of_files.items()):
        f.writelines(f".{extension}\n")
        for file in sorted(files):
            f.writelines(f"---{file}\n")

