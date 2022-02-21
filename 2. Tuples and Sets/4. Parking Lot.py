N=int(input())

carpark=set()

for _ in range(N):
    direction, reg_number=input().split(", ")
    if direction=="IN":
        carpark.add(reg_number)
    else:
        carpark.remove(reg_number)
if len(carpark)==0:
    print("Parking Lot is Empty")
else:
    for car in carpark:
        print(car)
