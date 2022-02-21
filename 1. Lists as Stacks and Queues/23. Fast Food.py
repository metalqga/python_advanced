total_food=int(input())
orders=list(map(int, input().split()))
print(max(orders))
for _ in range(len(orders)):
    current_order=(orders[0])
    if current_order<=total_food:
        total_food-=current_order
        orders.pop(0)
    else:
        break
if len(orders)==0:
    print("Orders complete")
else:
    print(f"Orders left: ",end="")
    while len(orders)>0:
        if len(orders)>0:
            print(orders.pop(0),end=" ")

       