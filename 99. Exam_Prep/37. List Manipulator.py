def list_manipulator(*args):
    working_list = []
    add = False
    remove = False

    for i in range(len(args)):
        if type(args[i]) == list:
            working_list = args[i]
        elif args[i] == "add":
            add = True
        elif args[i] == "remove":
            remove = True

        elif args[i] == "beginning":
            if remove and i == len(args) - 1:
                working_list.pop(0)
                continue

            if add:
                for j in range(len(args) - 1, i, -1):
                    working_list.insert(0, args[j])
            elif remove:
                for j in range(args[i + 1]):
                    working_list.pop(0)


        elif args[i] == "end":
            if remove and i == len(args) - 1:
                working_list.pop(-1)
                continue

            if add:
                for j in range(i + 1, len(args)):
                    working_list.append(args[j])
            elif remove:
                for j in range(args[i + 1]):
                    working_list.pop()

    return working_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))  #
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))  #
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
