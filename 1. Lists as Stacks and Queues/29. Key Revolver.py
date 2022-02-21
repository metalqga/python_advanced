from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
value = int(input())

locks = deque(locks)
shots = len(bullets)
counter = 0

while locks and bullets:
    shots -= 1
    counter += 1
    if bullets[-1] <= locks[0]:
        print("Bang!")
        bullets.pop()
        if counter % barrel_size == 0 and bullets:
            print("Reloading!")
        locks.popleft()
    else:
        print("Ping!")
        bullets.pop()
        if counter % barrel_size == 0 and bullets:
            print("Reloading!")

if not locks:
    print(f'{shots} bullets left. Earned ${value - bullet_price * counter}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
