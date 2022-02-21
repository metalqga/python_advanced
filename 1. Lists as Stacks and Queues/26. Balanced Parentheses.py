parenteses = input()
stack=[]


for i in range(len(parenteses)):
    if parenteses[i]=="(" or parenteses[i]=="{" or parenteses[i]=="[":
        stack.append(parenteses[i])
    if len(stack)>0:
        if (parenteses[i]==")" and stack[-1]=="(") or (parenteses[i]=="}" and stack[-1]=="{") or (parenteses[i]=="]" and stack[-1]=="["):
            stack.pop()
    else:
        stack.append(parenteses[i])

if len(stack)>0:
    print("NO")
else:
    print("YES")


#
#
# if parenteses=="":
#     print("NO")
#     exit()
# left_half = parenteses[:(len(parenteses) // 2)]
# for i in range(len(left_half)):
#     left_stack.append(left_half[i])
#
# right_half = parenteses[(len(parenteses) // 2):]
# for j in range(len(right_half)):
#     right_stack.append(right_half[j])
#
# for k in range(len(left_stack)):
#     if left_stack[-1] == "(":
#         if right_stack[0] == ")":
#             left_stack.pop()
#             right_stack.pop(0)
#
#     elif left_stack[-1] == "{":
#         if right_stack[0] == "}":
#             left_stack.pop()
#             right_stack.pop(0)
#
#     elif left_stack[-1] == "[":
#         if right_stack[0] == "]":
#             left_stack.pop()
#             right_stack.pop(0)
# if len(left_stack) > 0 or len(right_stack)>0:
#     sequence_check=left_stack+right_stack
#     for i in range(len(sequence_check)-1):
#         if len(sequence_check)==0:
#             break
#         elif sequence_check[0]=="(" and sequence_check[1]==")":
#             sequence_check.pop(0)
#             sequence_check.pop(0)
#         elif sequence_check[0]=="[" and sequence_check[1]=="]":
#             sequence_check.pop(0)
#             sequence_check.pop(0)
#         elif sequence_check[0]=="{" and sequence_check[1]=="}":
#             sequence_check.pop(0)
#             sequence_check.pop(0)
#
#     if len(sequence_check)>0:
#         print("NO")
#     else:
#         print("YES")
# else:
#     print("YES")