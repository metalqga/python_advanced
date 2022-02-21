N=int(input())

usernames=set()

for _ in range(N):
    username=input()
    usernames.add(username)

for username in usernames:
    print(username)