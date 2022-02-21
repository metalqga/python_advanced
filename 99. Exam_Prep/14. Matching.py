from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while True:
    if not males or not females:
        break
    male = males[-1]

    if male <= 0 and males:
        males.pop()
        continue

    female = females[0]
    while female <= 0 and females:
        females.popleft()
        continue

    if male % 25 == 0:
        if males:
            males.pop()

        else:
            break
        if males:
            males.pop()
            continue

    if female % 25 == 0:
        if females:
            females.popleft()
        else:
            break
        if females:
            females.popleft()
            continue

    if male == female:
        matches += 1
        if males:
            males.pop()
        if females:
            females.popleft()

    else:
        if females:
            females.popleft()
        else:
            break
        males[-1] = male - 2


print(f"Matches: {matches}")
if males:
    males = reversed([str(x) for x in males])
    print(f"Males left: {(', ').join(males)}")
else:
    print("Males left: none")
if females:
    females = [str(x) for x in females]
    print(f"Females left: {(', ').join(females)}")
else:
    print("Females left: none")
