n = int(input())
matrix = []
bomb_psn = []
alive_cells = 0
sum_of_cells = 0
for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

bombs = input().split()
for bomb in bombs:
    bomb = bomb.split(",")
    bomb_psn.append([int(bomb[0]), int(bomb[1])])

for bomb in bomb_psn:
    bomb_power = matrix[bomb[0]][bomb[1]]
    #
    if bomb_power > 0:
        for row in range(bomb[0] - 1, bomb[0] + 2):
            for col in range(bomb[1] - 1, bomb[1] + 2):
                if 0 <= row < n and 0 <= col < n:
                    if matrix[row][col] > 0:
                        matrix[row][col] -= bomb_power
        matrix[bomb[0]][bomb[1]] = 0
    else:
        continue
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_cells += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
