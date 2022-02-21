from collections import deque

N, M = [int(x) for x in input().split()]

matrix = []
player_psn = []
bunny_psn = []
movements = deque()
dead = False

def print_state(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end="")
        print()

def movement(command, position, size1, size2, field):

    field[position[0]][position[1]] = "."
    bunny_multiplication(bunny_psn, field, size1, size2)
    if command == "U":
        if position[0] - 1 >= 0:
            position[0] -= 1
        else:
            update_state(field)
            print_state(field)
            print(f"won: {position[0]} {position[1]}")
            exit()

    elif command == "D":
        if position[0] + 1 < size1:  #
            position[0] += 1
        else:
            update_state(field)
            print_state(field)
            print(f"won: {position[0]} {position[1]}")
            exit()

    elif command == "R":
        if position[1] + 1 < size2: #
            position[1] += 1
        else:
            update_state(field)
            print_state(field)
            print(f"won: {position[0]} {position[1]}")
            exit()

    elif command == "L":
        if position[1] - 1 >= 0:
            position[1] -= 1
        else:
            update_state(field)
            print_state(field)
            print(f"won: {position[0]} {position[1]}")
            exit()

    if field[position[0]][position[1]] == "B":
        print_state(field)
        print(f"dead: {position[0]} {position[1]}")
        exit()
    else:
        field[position[0]][position[1]] = "P"

    return position

def update_state(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "P":
                player_psn.append(row)
                player_psn.append(col)
            # elif matrix[row][col] == '':
            #     matrix[row][col] = "."
            elif matrix[row][col] == "B":
                bunny_psn.append([row, col])

def bunny_multiplication(bunny_psn, field, size1, size2):
    for position in bunny_psn:

        if (position[0] - 1) >= 0:
            field[(position[0] - 1)][position[1]] = "B"

        if (position[0] + 1) < size1:  #
            field[(position[0] + 1)][position[1]] = "B"

        if (position[1] + 1) < size2:  #
            field[position[0]][(position[1] + 1)] = "B"

        if (position[1] - 1) >= 0:
            field[position[0]][(position[1] - 1)] = "B"

######################

for _ in range(N):
    lines = input()
    temp = []
    for element in lines:
        temp.append(element)
    matrix.append(temp)
    temp = []

command = input()
for el in command:
    movements.append(el)

while movements:
    update_state(matrix)
    movement(movements.popleft(), player_psn, N, M, matrix)
    bunny_multiplication(bunny_psn, matrix, N, M)
    player_psn = []
    bunny_psn = []
    update_state(matrix)
    if not player_psn:
        dead = True
        break

print_state(matrix)
if dead:
    print("DEAD!")
    print_state(matrix)
