import os


def traverse_dir(path,files_by_ext):
    for element in os.listdir(path):
        if os.path.isdir(os.path.join(path,element)):
            traverse_dir(os.path.join(path,element),files_by_ext)
        else:
            extension=element.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension]=[]
            files_by_ext[extension].append(element)

files_by_ext=dict()
traverse_dir(".",files_by_ext)

with open(os.path.join(os.path.expanduser("~"),"Desktop", "report.txt"), "w") as output:
    for ext,files in sorted(files_by_ext.items()):
        output.write(f".{ext}\n")
        for file in files:
            output.write(f"- - - {file}\n")