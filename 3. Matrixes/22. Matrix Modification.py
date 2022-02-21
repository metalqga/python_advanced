rows = int(input())
matrix = []
for i in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

while True:
    command = input().split()
    if "Add" in command:
        row = int(command[1])
        col = int(command[2])
        val = int(command[3])

        if 0 <= row <= (len(matrix) - 1) and 0 <= col <= (len(matrix[row]) - 1):
            matrix[row][col] += val
        else:
            print("Invalid coordinates")

    elif "Subtract" in command:
        row = int(command[1])
        col = int(command[2])
        val = int(command[3])
        if 0 <= row <= (len(matrix) - 1) and 0 <= col <= (len(matrix[row]) - 1):
            matrix[row][col] -= val
        else:
            print("Invalid coordinates")

    elif "END" in command:
        break
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
