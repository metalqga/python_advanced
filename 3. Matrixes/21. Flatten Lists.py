# string=input().split("|")
#
#
# for i in range(len(string)-1,-1,-1):
#     print(*string[i].split(),end=" ")

strings=input().split("|")

while strings:
    string=strings.pop().split()
    if string:
        print(" ".join(string),end=" ")