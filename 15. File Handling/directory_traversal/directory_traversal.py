import os

files_by_ext=dict()
for root,dirs,files in os.walk("."):
    for file in files:
        extension=file.split(".")[-1]
        if extension not in files_by_ext:
            files_by_ext[extension]=[]
        files_by_ext[extension].append(file)

with open(os.path.join(os.path.expanduser("~"),"Desktop", "report.txt"), "w") as output:
    for ext,files in sorted(files_by_ext.items()):
        output.write(f".{ext}\n")
        for file in files:
            output.write(f"- - - {file}\n")