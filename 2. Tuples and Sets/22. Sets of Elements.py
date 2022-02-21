numbers=input().split()
n=int(numbers[0])
m=int(numbers[1])
n_set=set()
m_set=set()

for _ in range(n):
    num=int(input())
    n_set.add(num)
for _ in range(m):
    num = int(input())
    m_set.add(num)
for number in n_set&m_set:
    print(number)