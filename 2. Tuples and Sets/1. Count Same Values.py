numbers=input().split()
mydict={}

for i in range(len(numbers)):
    if float(numbers[i]) not in mydict:
        mydict[float(numbers[i])]=1
    else:
        mydict[float(numbers[i])]+=1
for num,count in mydict.items():
    print(f"{num:.1f} - {count} times")