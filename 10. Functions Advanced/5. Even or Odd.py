def even_odd(*nums):
    list=nums
    list1=[]
    command=nums[-1]

    if command=="even":
        for i in range(0,len(list)-1):
            if list[i]%2==0:
                list1.append(list[i])

    elif command == "odd":
        for i in range(0,len(list)-1):
            if list[i] % 2 != 0:
                list1.append(list[i])

    return list1

# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, "odd"))