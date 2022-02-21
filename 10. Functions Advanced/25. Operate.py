def operate(*args):
    result = 0
    if args[0]=="+":
        for i in range(1,len(args)):
            result+=args[i]
    elif args[0]=="-":
        result=args[1]
        for i in range(2,len(args)):
            result-=args[i]
    elif args[0]=="*":
        result=1
        for i in range(1, len(args)):
            result = result*args[i]
    elif args[0]=="/":
        for i in range(2,len(args)):
            result=args[1]
            result=f"{result/args[i]:.2f}"

    return result

print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 0, 1))