def odd_even(command,numbers):
    sum_even=0
    sum_odd=0
    numbers=list(map(lambda x: int(x), numbers))

    for i in range(len(numbers)):
        if numbers[i]%2==0:
            sum_even+=numbers[i]
        else:
            sum_odd+=numbers[i]

    if command=="Odd":
        print(sum_odd*len(numbers))
    elif command=="Even":
        print(sum_even*len(numbers))

command=input()
numbers=input().split()
odd_even(command,numbers)