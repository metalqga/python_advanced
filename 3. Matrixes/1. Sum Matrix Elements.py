rows,columns=[int(el) for el in input().split(", ")]
matrix=[]
sum1 = 0
for i in range(int(rows)):

    elements = [int(el) for el in input().split(", ")]
    sum1 += sum(elements)
    matrix.append(elements)


print(sum1)
print(matrix)