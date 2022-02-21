N=int(input())
matrix=[]
sum=0

for _ in range(N):
    nums=[int(el) for el in input().split()]
    matrix.append(nums)

for i in range(len(matrix)):
    sum+=matrix[i][i]
print(sum)