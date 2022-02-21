matrix = []
queens = []
king_psn = []
dangerous_queen = []


def if_dangerous(matrix, queens):
    dangerous = False
    for queen in queens:
        x = queen[0]
        y = queen[1]

        # check down
        for row in range(1, 7):
            if x + row > 7:
                break
            if matrix[x + row][y] == "Q":
                break
            elif matrix[x + row][y] == "K":
                dangerous_queen.append(queen)
                break

        # check up
        for row in range(1, 7):
            if x - row < 0:
                break
            if matrix[x - row][y] == "Q":
                break
            elif matrix[x - row][y] == "K":
                dangerous_queen.append(queen)
                break

        # check right
        for col in range(1, 7):
            if y + col > 7:
                break
            if matrix[x][y + col] == "Q":
                break
            elif matrix[x][y + col] == "K":
                dangerous_queen.append(queen)
                break

        # check left
        for col in range(1, 7):
            if y - col < 0:
                break
            if matrix[x][y - col] == "Q":
                break
            elif matrix[x][y - col] == "K":
                dangerous_queen.append(queen)
                break

        # check diagonal1 down
        for row in range(1, 8):
            col = row
            if x + row > 7 or y + col > 7:
                break
            if matrix[x + row][y + col] == "Q":
                break
            elif matrix[x + row][y + col] == "K":
                dangerous_queen.append(queen)
                break

        # check diagonal1 up
        for row in range(1, 8):
            col = row
            if x - row < 0 or y - col < 0:
                break
            if matrix[x - row][y - col] == "Q":
                break
            elif matrix[x - row][y - col] == "K":
                dangerous_queen.append(queen)
                break

        # check diagonal1 up
        for row in range(1, 8):
            col = row
            if x - row < 0 or y + col > 7:
                break
            if matrix[x - row][y + col] == "Q":
                break
            elif matrix[x - row][y + col] == "K":
                dangerous_queen.append(queen)
                break

        # check diagonal1 down
        for row in range(1, 8):
            col = row
            if x + row > 7 or y - col < 0:
                break
            if matrix[x + row][y - col] == "Q":
                break
            elif matrix[x + row][y - col] == "K":
                dangerous_queen.append(queen)
                break

for i in range(8):
    line = input().split()
    matrix.append(line)

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "K":
            king_psn.append(row)
            king_psn.append(col)
        elif matrix[row][col] == "Q":
            queens.append([row, col])

if_dangerous(matrix, queens)

if not dangerous_queen:
    print("The king is safe!")
else:
    for queen in dangerous_queen:
        print(queen)
