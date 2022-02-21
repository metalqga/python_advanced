from collections import deque
num_pizzas = 0
orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
orders = deque(orders)

while orders and employees:

    employee = employees.pop()
    pizzas = orders.popleft()

    while pizzas > 10 or pizzas <= 0 and orders:
        pizzas = orders.popleft()
        if (pizzas > 10 or pizzas <= 0) and len(orders)==0:
            break

    if len(orders) == 0 and (pizzas > 10 or pizzas <= 0):
        employees.append(employee)
        break

    if pizzas <= employee:
        num_pizzas += pizzas

    else:
        while pizzas > 0:
            if pizzas <= employee:
                num_pizzas += pizzas
                pizzas = 0
                break
            else:
                pizzas -= employee
                num_pizzas += employee
            if len(employees) == 0 and pizzas > 0:
                orders.insert(0, pizzas)
                break
            employee = employees.pop()

if not orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {num_pizzas}")
    if employees:
        employees = [str(x) for x in employees]
        print(f"Employees: {(', ').join(employees)}")

else:
    print(f"Not all orders are completed.")
    orders = [str(x) for x in orders]
    print(f"Orders left: {(', ').join(orders)}")
