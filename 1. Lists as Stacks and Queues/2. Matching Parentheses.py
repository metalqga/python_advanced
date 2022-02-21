text=input()
stack=[]
current=0
for i in range(len(text)):
    if text[i]=="(":
        stack.append(i)
    if text[i]==")":
        current=stack.pop()


        print(text[current:i+1])