lines = int(input())
matrix = []

for _ in range(lines):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)

matrix2 = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix2.append(matrix[i][j])

print(matrix2)
