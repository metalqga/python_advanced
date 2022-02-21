text=input()
stack=[]
for i in range(len(text)):
    stack.append(text[i])
for i in range(len(stack)):
    last=stack.pop()
    print(last,end="")
