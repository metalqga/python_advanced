n = int(input())
bombs_count = int(input())
matrix = []
bombs_psn = []

for _ in range(n):
    matrix.append(["."] * n)

for _ in range(bombs_count):
    psn = [int(x) for x in input().strip("()").split(", ")]
    x = psn[0]
    y = psn[1]
    matrix[x][y] = "*"
    bombs_psn.append(psn)

for row in range(n):
    for col in range(n):
        element = matrix[row][col]
        if element == "*":
            continue
        else:
            counter = 0
            for row_el in range(-1, 2):
                for col_el in range(-1, 2):
                    if (row + row_el) < 0 or (row + row_el) >= n or (col + col_el) < 0 or (col + col_el) >= n:
                        continue
                    if matrix[row + row_el][col + col_el] == "*":
                        counter += 1
            matrix[row][col] = counter

for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()
