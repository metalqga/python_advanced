set1=set([int(x) for x in input().split()])
set2=set([int(x) for x in input().split()])
N=int(input())
working_set=set()

for _ in range(N):
    command=input().split()

    for element in command:
        if not element.isalpha():
             working_set.add(int(element))

    if "Add" in command and "First" in command:
        set1=set1.union(working_set)
    elif "Add" in command and "Second" in command:
        set2=set2.union(working_set)
    elif "Remove" and "First" in command:
        set1=set1.difference(working_set)
    elif "Remove" in command and "Second" in command:
        set2=set2.difference(working_set)
    elif "Check" in command:
        print(set1.issubset(set2) or set2.issubset(set1))


    working_set=set()
print(*sorted(set1),sep=", ")
print(*sorted(set2),sep=", ")