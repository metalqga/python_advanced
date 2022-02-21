row = 6
col = 7
counter = 0
matrix = [[0 for i in range(col)] for j in range(row)]


def update_state(matrix, player, num):
    for i in range(row - 1, -1, -1):
        if matrix[i][num] == 0:
            matrix[i][num] = player
            update_state.current_row = i
            # update_state.current_column = num
            return


def print_state(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()


def check_winner(matrix, num, current_row, player, row, col):
    winner_counter = 0
    # left-right
    for i in range(0, 3):
        if num + i < col:
            if matrix[current_row][num + i] == player:
                winner_counter += 1
        if num - 1 - i >= 0:
            if matrix[current_row][num - 1 - i] == player:
                winner_counter += 1
    if winner_counter == 4:
        print(f"The winner is Player {player}")
        exit()
    # up-down
    winner_counter = 0
    for i in range(0, 4):
        if current_row + i < row:
            if matrix[current_row + i][num] == player:
                winner_counter += 1
    if winner_counter == 4:
        print(f"The winner is Player {player}")
        exit()
    winner_counter = 0
    # diagonal - up - right / down - left
    for i in range(0, 4):
        if num + i < col and current_row - i >= 0:
            if matrix[current_row - i][num + i] == player:
                winner_counter += 1
        if num - 1 - i >= 0 and (current_row + 1 + i) < row:
            if matrix[current_row + 1 + i][num - 1 - i] == player:
                winner_counter += 1
    if winner_counter == 4:
        print(f"The winner is Player {player}")
        exit()

    winner_counter = 0
    # diagonal - up - left / down - right
    for i in range(0, 4):
        if num - i <= 0 and current_row + i < row:
            if matrix[current_row + i][num - i] == player:
                winner_counter += 1
        if num + 1 + i < row and (current_row - 1 - i) >= 0:
            if matrix[current_row - 1 - i][num + 1 + i] == player:
                winner_counter += 1
    if winner_counter == 4:
        print(f"The winner is Player {player}")
        exit()


while True:
    if counter % 2 == 0:
        player = 1
    else:
        player = 2

    try:
        num = int(input(f"Player {player}, please choose a column \n")) - 1

    except ValueError:
        print("The column number must be an integer")
        continue

    if 0 <= num < col:
        if matrix[0][num] != 0:
            print(f"Column full! Please choose another column!")
            continue
        counter += 1
        update_state(matrix, player, num)
        print_state(matrix, row, col)
        check_winner(matrix, num, update_state.current_row, player, row, col)
    else:
        print(f"Please choose a number from 1 to {col}")