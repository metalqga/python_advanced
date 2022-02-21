string = input()
N = int(input())
matrix = []
player_psn = []
line1 = ""

for _ in range(N):
    line = input()
    for i in range(len(line)):
        line1 += line[i] + " "
    matrix.append(line1.split())
    line1 = ""

for row in range(N):
    for col in range(N):
        if matrix[row][col] == "P":
            player_psn.append(row)
            player_psn.append(col)

num2 = int(input())
for _ in range(num2):
    command = input()
    matrix[player_psn[0]][player_psn[1]] = "-"
    if command == "up":
        player_psn[0] -= 1
        if player_psn[0] < 0:
            string = string[:-1]
            player_psn[0] += 1
            continue

    elif command == "down":
        player_psn[0] += 1
        if player_psn[0] > N - 1:
            string = string[:-1]
            player_psn[0] -= 1
            continue

    elif command == "left":
        player_psn[1] -= 1
        if player_psn[1] < 0:
            string = string[:-1]
            player_psn[1] += 1
            continue

    elif command == "right":
        player_psn[1] += 1
        if player_psn[1] > N - 1:
            string = string[:-1]
            player_psn[1] -= 1
            continue

    if matrix[player_psn[0]][player_psn[1]] != "-":
        string += matrix[player_psn[0]][player_psn[1]]
    matrix[player_psn[0]][player_psn[1]] = "P"

matrix[player_psn[0]][player_psn[1]] = "P"
print(string)

for row in range(N):
    for col in range(N):
        print(matrix[row][col], end="")
    print()
