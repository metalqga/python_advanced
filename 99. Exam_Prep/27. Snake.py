n = int(input())
matrix = []
line1 = ""
snake_psn = []
burrows = []
food = 0

for _ in range(n):
    line = input()
    for i in range(len(line) - 1):
        line1 += line[i] + ","
    line1 += line[-1]
    matrix.append(line1.split(","))
    line1 = ""

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "S":
            snake_psn.append(row)
            snake_psn.append(col)
        elif matrix[row][col] == "B":
            burrows.append([row, col])

while True:
    if food >= 10:
        break
    command = input()
    x = snake_psn[0]
    y = snake_psn[1]
    matrix[x][y] = "."

    if command == "up":
        snake_psn[0] -= 1
        if snake_psn[0] < 0:
            break
    elif command == "down":
        snake_psn[0] += 1
        if snake_psn[0] >= n:
            break
    elif command == "left":
        snake_psn[1] -= 1
        if snake_psn[1] < 0:
            break
    elif command == "right":
        snake_psn[1] += 1
        if snake_psn[1] >= n:
            break

    x = snake_psn[0]
    y = snake_psn[1]

    if matrix[x][y] == "*":
        food += 1
        matrix[x][y] = "S"
    elif matrix[x][y] == "B":
        burrows.remove([x, y])
        matrix[x][y] = "."
        snake_psn[0] = burrows[0][0]
        snake_psn[1] = burrows[0][1]
        x = snake_psn[0]
        y = snake_psn[1]
        matrix[x][y] = "S"

if food >= 10:
    print(f"You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food}")
for row in range(n):
    for col in range(n):
        print(matrix[row][col], end="")
    print()
