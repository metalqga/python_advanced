def numbers_searching(*args):
    num_list = list(args)
    diff = []
    result = []
    for element in num_list:
        if num_list.count(element) > 1:
            if element not in diff:
                diff.append(element)
            num_list.remove(element)

    result.append(sorted(diff))
    num_list = sorted(num_list)
    for i in range(num_list[0], num_list[-1]):
        if i not in num_list:
            result.insert(0, i)

    return result


print(numbers_searching(50, 50, 46, 47, 48, 45, 46, 44, 47, 45, 44, 44, 48, 44, 48))
