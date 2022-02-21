import math

lines = int(input())
matrix = []
player_psn = []
player_path = []
score = 0

for _ in range(lines):
    line = input().split()
    matrix.append(line)

for row in range(lines):
    for col in range(len(matrix[0])):
        if matrix[row][col].isdigit():
            matrix[row][col] = int(matrix[row][col])

        elif matrix[row][col] == "P":
            player_psn.append(row)
            player_psn.append(col)

while True:
    player_path.append([player_psn[0], player_psn[1]])
    command = input()
    if command == "up":
        player_psn[0] -= 1
        if player_psn[0] < 0:
            player_psn[0] = len(matrix) - 1
    elif command == "down":
        player_psn[0] += 1
        if player_psn[0] > len(matrix) - 1:
            player_psn[0] = 0
    elif command == "left":
        player_psn[1] -= 1
        if player_psn[1] == -1:
            player_psn[1] = len(matrix[0]) - 1
    elif command == "right":
        player_psn[1] += 1
        if player_psn[1] > len(matrix[0]) - 1:
            player_psn[1] = 0

    if type(matrix[player_psn[0]][player_psn[1]]) == int:
        score += matrix[player_psn[0]][player_psn[1]]
        matrix[player_psn[0]][player_psn[1]] = "."

    if matrix[player_psn[0]][player_psn[1]] == "X":
        score = math.floor(score / 2)
        player_path.append([player_psn[0], player_psn[1]])
        break

    if score >= 100:
        player_path.append([player_psn[0], player_psn[1]])
        break

if score >= 100:
    print(f"You won! You've collected {score} coins.")
else:
    print(f"Game over! You've collected {score} coins.")
print(f"Your path:")
for psn in player_path:
    print(psn)
