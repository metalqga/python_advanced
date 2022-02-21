def fx(numbers):
    sum_pos=0
    sum_neg=0
    numbers=list(map(lambda x:int(x),numbers))

    for i in range(len(numbers)):
        if numbers[i]>0:
            sum_pos+=numbers[i]
        else:
            sum_neg+=numbers[i]
    print(sum_neg)
    print(sum_pos)
    if abs(sum_pos)>abs(sum_neg):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

numbers=input().split()
fx(numbers)