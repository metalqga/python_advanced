from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = ([int(x) for x in input().split()])
symbols = deque(input().split())
honey = 0
end=False

while bees and nectar:
    result = 0

    while bees[0] > nectar[-1]:
        nectar.pop()
        if len(nectar) == 0:
            end=True
            break
    if end:
        break
    if bees[0]<=nectar[-1]:
        if symbols[0] == "+":
            result = bees[0] + nectar[-1]
        elif symbols[0] == "-":
            result = bees[0] - nectar[-1]
        elif symbols[0] == "*":
            result = bees[0] * nectar[-1]
        elif symbols[0] == "/" and nectar[-1]!=0:
            result = bees[0] / nectar[-1]
        bees.popleft()
        nectar.pop()
        symbols.popleft()
        honey += abs(result)

print(f"Total honey made: {honey}")
if len(bees) > 0:
    print(f"Bees left: ", end="")
    print(*bees, sep=", ")
if len(nectar) > 0:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")
