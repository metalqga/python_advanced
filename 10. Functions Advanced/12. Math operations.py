from collections import deque
def math_operations(*args,**kwargs):
    list=[]
    dict={}
    nums=deque(args)
    while nums:
        kwargs["a"]+=nums.popleft()
        if len(nums)==0:
            break
        kwargs["s"]-=nums.popleft()
        if len(nums)==0:
            break
        divisor=nums.popleft()
        if divisor!=0:
            kwargs["d"]=kwargs["d"]/divisor
        if len(nums)==0:
            break
        kwargs["m"]=kwargs["m"]*nums.popleft()
    return kwargs
