r,c =[int(x) for x in input().split()]
matrix=[]

for row in range(r):
    for col in range(c):
        print(chr(97+row)+chr(97+row+col)+chr(97+row),end=" ")
    print()
