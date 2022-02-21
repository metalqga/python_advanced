n=int(input())
matrix=[]
sum_p=0
sum_s=0
primary_diagonal=[]
secondary_diagonal=[]

for _ in range(n):
    line=[int(x) for x in input().split(" ")]
    matrix.append(line)

for i in range(n):
    element1=matrix[i][i]
    element2=matrix[i][n-1-i]
    primary_diagonal.append(element1)
    secondary_diagonal.append(element2)
    sum_p+=element1
    sum_s+=element2
print(abs(sum_p-sum_s))