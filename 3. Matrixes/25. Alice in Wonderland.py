n = int(input())
territory = []
tea_bags = 0
alice_psn = []
hole_psn = []
for i in range(n):
    line = input().split()
    territory.append(line)

for row in range(len(territory)):
    for col in range(len(territory[row])):
        if territory[row][col] == "A":
            alice_psn.append(row)
            alice_psn.append(col)
        # elif territory[row][col].isdigit():
        #     territory[row][col]=int(territory[row][col])
        elif territory[row][col] == "R":
            hole_psn.append(row)
            hole_psn.append(col)
territory[alice_psn[0]][alice_psn[1]] = "*"
while True:

    command = input()
    if command == "up":
        alice_psn[0] -= 1
    elif command == "down":
        alice_psn[0] += 1
    elif command == "right":
        alice_psn[1] += 1
    elif command == "left":
        alice_psn[1] -= 1

    if alice_psn[0] < 0 or alice_psn[1] < 0:
        break
    if alice_psn[0] > (len(territory) - 1) or alice_psn[1] > (len(territory) - 1):
        break

    if territory[alice_psn[0]][alice_psn[1]].isnumeric():
        tea_bags += int(territory[alice_psn[0]][alice_psn[1]])
    territory[alice_psn[0]][alice_psn[1]] = "*"

    if alice_psn == hole_psn or tea_bags >= 10:
        territory[alice_psn[0]][alice_psn[1]] = "*"
        break


if tea_bags < 10 or alice_psn[0] < 0 or alice_psn[1] < 0:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for row in range(len(territory)):
    for col in range(len(territory[row])):
        print(territory[row][col], end=" ")
    print()
