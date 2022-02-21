import sys
rows, cols = [int(el) for el in input().split(", ")]
matrix=[]
max_sum=-sys.maxsize
max_matrix=[]
for _ in range(rows):
    elements=[int(el) for el in input().split(", ")]
    matrix.append(elements)

for i in range(rows-1):
    for j in range(cols-1):
        sum=(matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+ matrix[i+1][j+1])
        if sum>max_sum:
            max_matrix=[]
            max_sum=sum
            max_matrix.append([matrix[i][j],matrix[i][j+1]])
            max_matrix.append([matrix[i+1][j], matrix[i+1][j+1]])
for i in range(len(max_matrix)):

    for j in range(len(max_matrix[i])):
        print(max_matrix[i][j], end=" ")
    print()

print(max_sum)