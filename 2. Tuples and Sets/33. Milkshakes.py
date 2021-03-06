from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])
counter = 0

while chocolate and milk and counter < 5:

    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        counter += 1
        chocolate.pop()
        milk.popleft()

    else:
        chocolate[-1] = chocolate[-1] - 5
        milk.append(milk.popleft())

if counter == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if len(milk) == 0:
    milk.append("empty")
if len(chocolate) == 0:
    chocolate.append("empty")

print(f"Chocolate: ", end="")
print(*chocolate, sep=", ")
print(f"Milk: ", end="")
print(*milk, sep=", ")
