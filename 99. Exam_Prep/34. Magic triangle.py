def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    for k in range(3, n + 1):
        matrix.append([" "] * k)

    for row in range(2, n):
        for col in range(row + 1):
            if col == 0:
                matrix[row][col] = 1
            if col == row:
                matrix[row][col] = 1
            for i in range(1, n):
                if col == row - i:
                    if matrix[row][col] == " ":
                        matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
    return (matrix)




get_magic_triangle(6)
