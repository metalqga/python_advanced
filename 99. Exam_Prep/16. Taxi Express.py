from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    taxi = taxis.pop()
    customer = customers.popleft()

    if taxi >= customer:
        total_time += customer
    else:
        customers.insert(0,customer)

if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    customers = [str(x) for x in customers]
    print(f'Customers left: {", ".join(customers)}')
