from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]
dbomb = 0
cbomb = 0
sdbomb = 0
success = False

while effects and casings:
    if success:
        effects.popleft()
        casings.pop()
        success = False

    if effects:
        effect = effects[0]
    else:
        break

    if casings:
        casing = casings[-1]

    else:
        break

    result = effect + casing
    if result == 40:
        dbomb += 1
        success = True
    elif result == 60:
        cbomb += 1
        success = True
    elif result == 120:
        sdbomb += 1
        success = True

    while not success:
        casing -= 5
        result = effect + casing
        if result == 40:
            dbomb += 1
            success = True
        elif result == 60:
            cbomb += 1
            success = True
        elif result == 120:
            sdbomb += 1
            success = True

    if dbomb >= 3 and cbomb >= 3 and sdbomb >= 3:
        effects.popleft()
        casings.pop()
        print(f"Bene! You have successfully filled the bomb pouch!")
        break

if not (dbomb >= 3 and cbomb >= 3 and sdbomb >= 3):
    print("You don't have enough materials to fill the bomb pouch.")

if not effects:
    print("Bomb Effects: empty")

else:
    effects = [str(x) for x in effects]
    print(f"Bomb Effects: {', '.join(effects)}")

if not casings:
    print("Bomb Casings: empty")

else:
    casings = [str(x) for x in casings]
    print(f"Bomb Casings: {', '.join(casings)}")

print(f"Cherry Bombs: {cbomb}")
print(f"Datura Bombs: {dbomb}")
print(f"Smoke Decoy Bombs: {sdbomb}")
