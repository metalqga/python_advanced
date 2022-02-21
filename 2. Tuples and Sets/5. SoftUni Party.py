N=int(input())

res_book=set()

for _ in range(N):
    res_code=input()
    res_book.add(res_code)

while True:
    arrived=input()
    res_book.discard(arrived)
    if arrived=="END":
        break

print(len(res_book))
for guest in sorted(res_book):
    print(guest)