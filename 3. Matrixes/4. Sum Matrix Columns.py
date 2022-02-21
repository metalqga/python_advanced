lines,columns = [int(el) for el in input().split(", ")]
matrix = []
sum1=0
for _ in range(lines):
    nums = [int(el) for el in input().split(" ")]
    matrix.append(nums)

for row in range(columns):
    for column in range(len(matrix)):
        sum1+=(matrix[column][row])
    print(sum1)
    sum1=0



