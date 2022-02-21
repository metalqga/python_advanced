from collections import deque

n = int(input())
movements = input().split()
matrix = []
miner_psn = []
coal_psn = []
end_psn = []
movements = deque(movements)
coal = 0

for _ in range(n):
    line = input().split()
    matrix.append(line)


def movement(command, position, size, field):
    if command == "up":
        if position[0] - 1 >= 0:
            field[position[0]][position[1]] = "*"
            position[0] -= 1
    elif command == "down":
        if position[0] + 1 < size:
            field[position[0]][position[1]] = "*"
            position[0] += 1
    elif command == "right":
        if position[1] + 1 < size:
            field[position[0]][position[1]] = "*"
            position[1] += 1
    elif command == "left":
        if position[1] - 1 >= 0:
            field[position[0]][position[1]] = "*"
            position[1] -= 1

    field[position[0]][position[1]] = "s"
    return position


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "s":
            miner_psn.append(row)
            miner_psn.append(col)

        elif matrix[row][col] == "c":
            coal_psn.append([row, col])

        elif matrix[row][col] == "e":
            end_psn.append(row)
            end_psn.append(col)
total_coal = len(coal_psn)

while movements:
    movement(movements.popleft(), miner_psn, n, matrix)
    if miner_psn == end_psn:
        print(f"Game over! ({miner_psn[0]}, {miner_psn[1]})")
        exit()
    elif miner_psn in coal_psn:
        coal += 1
        coal_psn.remove(miner_psn)
    if coal >= total_coal:
        print(f"You collected all coal! ({miner_psn[0]}, {miner_psn[1]})")
        exit()

if coal < total_coal:
    print(f"{total_coal - coal} pieces of coal left. ({miner_psn[0]}, {miner_psn[1]})")
