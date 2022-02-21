from _collections import deque
kids=input().split()
nth_toss=int(input())
players=deque(kids)

while len(players)>1:
    players.rotate(-nth_toss)
    print(f"Removed {players.pop()}")

print(f"Last is {players.pop()}")