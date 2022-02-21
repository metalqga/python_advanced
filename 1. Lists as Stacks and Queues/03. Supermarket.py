queue=[]

while True:
    name=input()

    if name=="End":
        break
    elif name=="Paid":
        for _ in range(len(queue)):
            last=queue.pop(0)
            print(last)
    else:
        queue.append(name)
print(f"{len(queue)} people remaining.")
