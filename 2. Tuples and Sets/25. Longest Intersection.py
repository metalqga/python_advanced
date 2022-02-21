N=int(input())

max_intersection=0
longest_intersection=set()
list1=[]
list2=[]
set1=set()
set2=set()
str=""

for i in range(N):
    range1=input()
    for element in range1:
        if element==",":
            list2.append(int(str))
            str = ""
        elif element=="-":
            list2.append(int(str))
            str = ""
            list1=list2
            list2=[]
        else:
            str+=element

    list2.append(int(str))
    str=""

    for i in range(list1[0],list1[1]+1):
        set1.add(i)

    for j in range(list2[0],list2[1]+1):
        set2.add(j)

    intersection=len(set1.intersection(set2))
    if intersection>max_intersection:
        max_intersection=intersection
        longest_intersection=set1.intersection(set2)

    list1=[]
    list2=[]
    set1=set()
    set2=set()

longest_intersection_list=list(longest_intersection)

print(f"Longest intersection is {longest_intersection_list} with length {max_intersection}")