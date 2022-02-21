n=int(input())

table=set()

for _ in range(n):
    chemicals=input().split()
    for chemical in chemicals:
        table.add(chemical)

for chemical in table:
    print(chemical)