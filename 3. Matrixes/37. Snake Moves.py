m, n = [int(x) for x in input().split()]
string = input()
matrix = []
index = 0
row = 0
string1 = ""

while row < m:
    string1 += (string[index])
    index += 1

    if len(string1) == n:
        if row % 2 == 0:
            matrix.append(string1)
        else:
            matrix.append(string1[::-1])
        row += 1
        string1 = ""
    if index == len(string):
        index = 0

print(*matrix,sep= "\n")
