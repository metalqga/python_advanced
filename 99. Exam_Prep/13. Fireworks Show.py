from collections import deque

fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]
fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while fireworks_effects and explosive_power:
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        break
    current_effect = fireworks_effects.popleft()
    while current_effect <= 0 and fireworks_effects:
        current_effect = fireworks_effects.popleft()

    current_power = explosive_power.pop()
    while current_power <= 0 and explosive_power:
        current_power = explosive_power.pop()

    result = current_effect + current_power

    if current_power <= 0:
        if current_effect > 0:
            fireworks_effects.insert(0, current_effect)
        break

    if current_effect <= 0:
        if  current_power >0:
            explosive_power.append(current_power)
        break


    if result % 3 == 0 and result % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks["Willow Fireworks"] += 1
    elif result % 5 == 0 and result % 3 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        current_effect = current_effect - 1
        fireworks_effects.append(current_effect)
        explosive_power.append(current_power)

if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    fireworks_effects = [str(x) for x in fireworks_effects]
    print(f"Firework Effects left: {', '.join(fireworks_effects)}")
if explosive_power:
    explosive_power = [str(x) for x in explosive_power]
    print(f"Explosive Power left: {', '.join(explosive_power)}")

for firework, num in fireworks.items():
    print(f"{firework}: {num}")
