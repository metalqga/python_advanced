from collections import deque

fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

pf=0
wf=0
cf=0

while fireworks_effects and explosive_power:
    if pf >= 3 and wf >= 3 and cf >= 3:
        break

    current_effect = fireworks_effects.popleft()
    while current_effect <= 0 and fireworks_effects:
        current_effect = fireworks_effects.popleft()
    if current_effect<=0:
        break

    current_power = explosive_power.pop()
    while current_power <= 0 and explosive_power:
        current_power = explosive_power.pop()
    if current_power<=0:
        fireworks_effects.insert(0,current_effect)
        break
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
        pf += 1
    elif result % 5 == 0 and result % 3 != 0:
        wf += 1
    elif result % 5 == 0 and result % 3 == 0:
        cf += 1
    else:
        current_effect = current_effect - 1
        fireworks_effects.append(current_effect)
        explosive_power.append(current_power)

if pf >= 3 and wf >= 3 and cf >= 3:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    fireworks_effects = [str(x) for x in fireworks_effects]
    print(f"Firework Effects left: {', '.join(fireworks_effects)}")
if explosive_power:
    explosive_power = [str(x) for x in explosive_power]
    print(f"Explosive Power left: {', '.join(explosive_power)}")

print(f"Palm Fireworks: {pf}")
print(f"Willow Fireworks: {wf}")
print(f"Crossette Fireworks: {cf}")
