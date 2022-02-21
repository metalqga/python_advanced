import sys


def best_list_pureness(*args):
    best_pureness = -sys.maxsize
    best_rotation = 0
    pureness = 0
    list1 = args[0]
    n = args[1]

    for i in range(n+1):
        for j in range(len(list1)):
            pureness += j * list1[j]
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = i
        pureness = 0
        list1.insert(0, list1.pop())

    return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
