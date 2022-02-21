r, c = [int(x) for x in input().split()]
matrix = []
temp = 0

for _ in range(r):
    items = input().split()
    matrix.append(items)

while True:
    command = input().split()
    if "END" in command:
        break

    elif len(command) != 5:
        print("Invalid input!")

    elif "swap" in command and command[0]=="swap":
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])

        if row1 > r or col1 > c or row2 > r or col2 > c:
            print("Invalid input!")
        elif row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
            print("Invalid input!")
        else:
            temp = matrix[row2][col2]
            matrix[row2][col2] = matrix[row1][col1]
            matrix[row1][col1] = temp
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end=" ")
                print()

    else:
        print("Invalid input!")