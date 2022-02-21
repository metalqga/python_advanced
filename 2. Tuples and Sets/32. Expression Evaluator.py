from collections import deque
str=input().split()
result=0
nums=deque()
result=0
for element in str:
    if element in "+-*/":
        while len(nums)>1:
            first=nums.popleft()
            second=nums.popleft()


            if element == "-":
                result = first-second

            elif element == "+":
                result = first+second

            elif element == "/":
                result = first // second

            elif element == "*":
                result = first*second
            nums.appendleft(result)

    else:
        nums.append(int(element))




print(result)