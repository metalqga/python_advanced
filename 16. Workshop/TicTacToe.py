def coordinates(psn):
    if psn == 1:
        return 0, 1
    elif psn == 2:
        return 0, 3
    elif psn == 3:
        return 0, 5
    elif psn == 4:
        return 1, 1
    elif psn == 5:
        return 1, 3
    elif psn == 6:
        return 1, 5
    elif psn == 7:
        return 2, 1
    elif psn == 8:
        return 2, 3
    elif psn == 9:
        return 2, 5


def update_state(matrix, symbol, psn):
    position = coordinates(psn)
    if (matrix[position[0]][position[1]]) == " ":
        matrix[position[0]][position[1]] = symbol
    else:
        print("Position occupied, please try again!")


def print_state(matrix):
    for row in range(3):
        for col in range(7):
            print(matrix[row][col], end=" ")
        print()


def check_winner(matrix, player_symbol, current_player):
    # check rows
    for i in range(0, 3):
        winner_counter = 0
        for j in range(0, 6, 1):
            if matrix[i][j] == player_symbol:
                winner_counter += 1
            if winner_counter == 3:
                print(f"The winner is Player {current_player}")
                exit()
    # check columns
    for i in range(0, 6, 1):
        winner_counter = 0
        for j in range(3):
            if matrix[j][i] == player_symbol:
                winner_counter += 1
            if winner_counter == 3:
                print(f"The winner is Player {current_player}")
                exit()
        # check diagonal1
        if matrix[0][1] == player_symbol and matrix[1][3] == player_symbol and matrix[2][5] == player_symbol:
            print(f"The winner is Player {current_player}")
            exit()
        # check diagonal2
        if matrix[0][5] == player_symbol and matrix[1][3] == player_symbol and matrix[2][1] == player_symbol:
            print(f"The winner is Player {current_player}")
            exit()


def play(matrix, current_payer, current_symbol, psn):
    counter = 0

    while True:
        if counter % 2 == 0:
            current_player = player2
            current_symbol = player2_symbol
        else:
            current_player = player1
            current_symbol = player1_symbol
        try:
            psn = int(input(f"{current_player} choose a free position [1-9]"))
        except ValueError:
            print("Try again! Choose a digit from 1 to 9!")
            psn = int(input(f"{player1} choose a free position [1-9]"))

        while psn <= 0 or psn > 9:
            print("Invalid choince, please try again!")
            psn = int(input(f"{current_player} choose a free position [1-9]"))

        position = coordinates(psn)

        if (matrix[position[0]][position[1]]) != " ":
            print("Place occupied, please choose again!")

        else:
            update_state(matrix, current_symbol, psn)
            print_state(matrix)
            check_winner(matrix, current_symbol, current_player)
            counter += 1
            if counter == 8:
                print("Neither side won, it was a draw!")
                exit()


#def setup():
player1 = input("Player one name: ")
player2 = input("Player two name: ")

player1_symbol = input(f"{player1} would you like to play with 'X' or 'O'? ")
while player1_symbol not in "XO":
    print("Invalid choice, please try again!")
    player1_symbol = input(f"{player1} would you like to play with 'X' or 'O'? ")

if player1_symbol == "X":
    player2_symbol = "O"

else:
    player2_symbol = "X"
matrix = [["|", "1", "|", "2", "|", "3", "|"], ["|", "4", "|", "5", "|", "6", "|"], ["|", "7", "|", "8", "|", "9", "|"]]
print_state(matrix)
matrix = [["|", " ", "|", " ", "|", " ", "|"], ["|", " ", "|", " ", "|", " ", "|"], ["|", " ", "|", " ", "|", " ", "|"]]

print((f"{player1} starts first!"))

try:
    psn = int(input(f"{player1} choose a free position [1-9]"))

except ValueError:
    print("Try again! Choose a digit from 1 to 9!")
    psn = int(input(f"{player1} choose a free position [1-9]"))

while psn <= 0 or psn > 9:
    print("Invalid choince, please try again!")
    psn = int(input(f"{player1} choose a free position [1-9]"))

current_player = player1
current_symbol = player1_symbol
update_state(matrix, current_symbol, psn)
print_state(matrix)
play(matrix,current_player,current_symbol,psn)
