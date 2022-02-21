matrix = []
w_psn = []
b_psn = []


def square(psn):
    letter = ""
    if psn == 0:
        letter = "a"
    elif psn == 1:
        letter = "b"
    elif psn == 2:
        letter = "c"
    elif psn == 3:
        letter = "d"
    elif psn == 4:
        letter = "e"
    elif psn == 5:
        letter = "f"
    elif psn == 6:
        letter = "g"
    elif psn == 7:
        letter = "h"
    return letter


for _ in range(8):
    line = input().split()
    matrix.append(line)

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            w_psn.append(row)
            w_psn.append(col)
        elif matrix[row][col] == "b":
            b_psn.append(row)
            b_psn.append(col)

for i in range(7):
    x = w_psn[0]
    y = w_psn[1]
    matrix[x][y]="-"

    if (y-1)>=0:
        if matrix[x - 1][y - 1] == "b":
            print(f"Game over! White win, capture on {square(y - 1)}{8 - x + 1}.")
            matrix[x-1][y-1] = "w"
            break
    if (y+1)<=7:
        if matrix[x - 1][y + 1] == "b":
            print(f"Game over! White win, capture on {square(y + 1)}{8 - x + 1}.")
            matrix[x-1][y+1] = "w"
            break

    x -= 1
    w_psn[0] = x
    matrix[x][y] = "w"

    if w_psn[0] <= 0:
        matrix[x][y] = "w"
        print(f"Game over! White pawn is promoted to a queen at {square(w_psn[1])}8.")
        break

    x = b_psn[0]
    y = b_psn[1]
    matrix[x][y]="-"

    if (y-1) >= 0:
        if matrix[x + 1][y - 1] == "w":
            print(f"Game over! Black win, capture on {square(y - 1)}{7-x}.")
            matrix[x + 1][y - 1] = "b"
            break
    if (y+1)<=7:
        if matrix[x + 1][y + 1] == "w":
            print(f"Game over! Black win, capture on {square(y + 1)}{7-x}.")
            matrix[x + 1][y + 1] = "b"
            break

    x += 1
    b_psn[0] = x
    matrix[x][y] = "b"

    if b_psn[0] >= 7:
        print(f"Game over! Black pawn is promoted to a queen at {square(b_psn[1])}1.")
        break