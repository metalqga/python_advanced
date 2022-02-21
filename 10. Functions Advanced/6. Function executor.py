def func_executor(*args):
    list=[]
    for func, arg in args:
        result=func(*arg)
        list.append(result)
    return list



def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))