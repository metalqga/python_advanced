stack=[]
N=int(input())
for i in range(N):
    query=input().split()
    if query[0]=="1":
        stack.append(int(query[1]))
    elif query[0]=="2" and len(stack)>0:
        stack.pop()
    elif query[0]=="3" and len(stack)>0:
        print(max(stack))
    elif query[0]=="4" and len(stack)>0:
        print(min(stack))
if len(stack)>=2:
    for _ in range(len(stack)-1):
        print(stack.pop(),end=", ")
    print(stack[0])
elif len(stack)==0:
    exit()
else:
    print(stack[0])