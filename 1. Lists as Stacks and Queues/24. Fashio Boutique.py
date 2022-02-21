clothes_pile=list(map(int,input().split()))
capacity=int(input())
current_capacity=0
racks=1

if sum(clothes_pile)==0:
    print("0")
    exit()

while len(clothes_pile)>0:
    current_capacity += clothes_pile[-1]
    if current_capacity<capacity:
        clothes_pile.pop()
    elif current_capacity==capacity:
        current_capacity=0
        clothes_pile.pop()
        if len(clothes_pile)>0:
            racks += 1
    else:
        current_capacity=0
        racks+=1

print(racks)