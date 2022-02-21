matrix = []
bullseye = []
counter = 0
p1_score = 501
p2_score = 501
p1_shots = 0
p2_shots = 0

player1, player2 = input().split(", ")
for _ in range(7):
    line = input().split()
    matrix.append(line)

for row in range(7):
    for col in range(7):
        if matrix[row][col] == "B":
            bullseye.append(str((row, col)))

while True:
    score = 0
    counter += 1

    if counter % 2 == 1:
        player = player1
        p1_shots += 1
    else:
        player = player2
        p2_shots += 1

    shot = input()

    if shot in bullseye:
        if player==player1:
            print(f"{player} won the game with {(p1_shots)} throws!")
        else:
            print(f"{player} won the game with {(p2_shots)} throws!")
        break

    shot = shot.strip("()").split(", ")
    x=int(shot[0])
    y=int(shot[1])
    if x<0 or y<0:
        continue
    elif x>6 or y>6:
        continue

    if matrix[x][y].isdigit():
        if player == player1:
            p1_score -= int(matrix[x][y])
        else:
            p2_score -= int(matrix[x][y])

    elif matrix[x][y] == "D":
        score = (int(matrix[x][0]) + int(matrix[x][6]) + int(matrix[0][y]) + int(matrix[6][y])) * 2
        if player == player1:
            p1_score -= score
        else:
            p2_score -= score
    elif matrix[x][y] == "T":
        score = (int(matrix[x][0]) + int(matrix[x][6]) + int(matrix[0][y]) + int(matrix[6][y])) * 3
        if player == player1:
            p1_score -= score
        else:
            p2_score -= score

    if p1_score <= 0:
        print(f"{player} won the game with {(p1_shots)} throws!")
        break
    elif p2_score <= 0:
        print(f"{player} won the game with {(p2_shots):.0f} throws!")
        break

# print(p1_score)
# print(p2_score)
