N=int(input())
matrix=[]

for _ in range(N):
    symbols=input()
    matrix.append(symbols)

special_symbol=input()

for row in range (len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col]==special_symbol:
            print(f"({row}, {col})")
            exit()

print(f"{special_symbol} does not occur in the matrix")