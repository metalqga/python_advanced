from collections import deque

cups = [int(x) for x in input().split()]
bottles = [int(x) for x in input().split()]
cups = deque(cups)
wasted = 0

while cups and bottles:
    if bottles[-1] < cups[0]:
        cups[0] = cups[0] - bottles[-1]
        bottles.pop()
    else:
        bottles[-1] = bottles[-1] - cups[0]
        cups.popleft()
        wasted += bottles[-1]
        bottles.pop()

if not cups:
    print(f"Bottles:", end=" ")
    for bottle in bottles:
        print(bottle, end=" ")
    print()
if not bottles:
    print(f"Cups:", end=" ")
    for cup in cups:
        print(cup, end=" ")
    print()
print(f"Wasted litters of water: {wasted}")
