rows,cols=[int(x) for x in input().split()]
matrix=[]
sum=0
for i in range(rows):
    chars=input().split()
    matrix.append(chars)

for i in range(rows-1):
    for j in range(cols-1):
        if matrix[i][j]==matrix[i+1][j]== matrix[i][j+1]==matrix[i+1][j+1]:
            sum+=1
print(sum)

