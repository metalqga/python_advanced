lines = int(input())
matrix = []

for i in range(lines):
    nums = [int(el) for el in input().split(", ")]

    matrix.append(nums)

matrix2 = []
for i in range(len(matrix)):
    matrix2.append([])
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            matrix2[i].append(matrix[i][j])

print(matrix2)
