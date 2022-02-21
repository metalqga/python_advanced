import sys
rows,cols=[int(x) for x in input().split()]
matrix=[]
best_row=0
best_col=0


max_sum=-sys.maxsize
current_sum=0
for _ in range(rows):
    nums=[int(x) for x in input().split()]
    matrix.append(nums)


for i in range(rows-2):
    for j in range(cols-2):
        current_sum=matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+ matrix[i+1][j]+matrix[i+1][j+1]+matrix[i+1][j+2]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
        if current_sum>max_sum:
            max_sum=current_sum
            best_row=i
            best_col=j

print(f"Sum = {max_sum}")
for i in range(3):
    for j in range(3):
        print(matrix[best_row+i][best_col+j], end=" ")
    print()

