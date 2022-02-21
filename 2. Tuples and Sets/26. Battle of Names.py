N=int(input())

to_print=[]
odd_set=set()
even_set=set()
sum=0
even_sum=0
odd_sum=0

for i in range(1,N+1):
    name=input()
    for j in range(len(name)):
        sum+=ord(name[j])
    result=sum//(i)
    if result%2==0:
        #even_sum+=result
        even_set.add(result)
    else:
        odd_set.add(result)
        #odd_sum+=result
    sum=0
for element in  odd_set:
    odd_sum+=element
for element in even_set:
    even_sum+=element

if odd_sum==even_sum:
    result=odd_set.union(even_set)
    for element in result:
        to_print.append(str(element))
    print((", ").join(to_print))

elif odd_sum>even_sum:
    result=odd_set.difference(even_set)
    for element in result:
        to_print.append(str(element))
    print((", ").join(to_print))

elif odd_sum<even_sum:
    result=odd_set.symmetric_difference(even_set)
    for element in result:
        to_print.append(str(element))
    print((", ").join(to_print))
