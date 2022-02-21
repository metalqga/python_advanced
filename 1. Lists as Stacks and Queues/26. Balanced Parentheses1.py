parenteses = input()
stack=[]
if len(parenteses)==0:
    print("NO")
    exit()
for i in range(len(parenteses)):
    if parenteses[i]=="(":
        stack.append(parenteses[i])
    elif parenteses[i]=="{":
        stack.append(parenteses[i])
    elif parenteses[i]=="[":
        stack.append(parenteses[i])
    if len(stack)==0:
        break
    if parenteses[i]==")":
        if stack[-1]=="(":
            stack.pop()
    elif parenteses[i]=="]":
        if stack[-1]=="[":
            stack.pop()
    elif parenteses[i]=="}":
        if stack[-1]=="{":
            stack.pop()

if len(stack)>0:
    print("NO")
else:
    print("YES")