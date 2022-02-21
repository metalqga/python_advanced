def stock_availability(*args):
    inventory = []
    sell = False
    deliver = False

    for i in range(len(args)):
        if deliver:
            inventory.append(args[i])
        elif sell:
            while args[i] in inventory:
                inventory.remove(args[i])
            if type(args[i]) == int:
                for _ in range(args[i]):
                    inventory.pop(0)
        if type(args[i]) == list:
            inventory = args[i]

        elif args[i] == "delivery":
            deliver = True

        elif args[i] == "sell":
            sell = True
            if i == len(args) - 1:
                inventory.pop(0)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
