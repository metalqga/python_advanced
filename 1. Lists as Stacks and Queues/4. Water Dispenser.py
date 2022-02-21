qtty=int(input())
names=[]
water_rq=[]
while True:
    name=input()
    if name=="Start":
        break
    else:
        names.append(name)

while True:
    command=input().split()
    if "End" in command:
        break
    elif "refill" in command:
        qtty+=int(command[1])
    else:
        if int(command[0])<=qtty:
            print(f"{names.pop(0)} got water")
            qtty -= int(command[0])
        else:
            print(f"{names.pop(0)} must wait")



print(f"{qtty} liters left")