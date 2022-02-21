from collections import deque

N=int(input())
diff=deque()
fuel=0

for _ in range(N):
    info=list(map(int, input().split()))
    diff.append(info[0]-info[1])


for i in range(N): #attempts
    for j in range(N):
        fuel+=diff[j]

        if fuel<0:
            break
    if fuel>0:
        print(i)
        break
    diff.rotate(-1)
    fuel = 0