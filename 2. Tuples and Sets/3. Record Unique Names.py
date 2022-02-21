N=int(input())

names=set()

for _ in range(N):
    name=input()
    names.add(name)

for name in names:
    print(name)