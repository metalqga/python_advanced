N=int(input())

logbook={}

for _ in range(N):
    name,grade=input().split()

    if name not in logbook:
        logbook[name]=[float(grade)]
    else:
        logbook[name].append(float(grade))

for name,grade in logbook.items():
    print(f"{name} -> ",end="")
    for i in range(len(grade)):
        print(f"{grade[i]:.2f} ",end="")
    print(f"(avg: {(sum(grade)/len(grade)):.2f})")

