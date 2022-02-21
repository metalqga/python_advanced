from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
toys = {}

while len(materials) > 0 and len(magic) > 0:
    if len(magic) == 1 and magic[0] == 0:
        magic.popleft()
        break
    if len(materials) == 1 and materials[0] == 0:
        materials.pop()
        break

    current_material = materials.pop()
    current_magic = magic.popleft()
    if current_magic == 0 and len(magic) > 0:
        current_magic = magic.popleft()

    if current_material == 0 and len(materials) > 0:
        current_material = materials.pop()

    result = current_magic * current_material

    if result < 0:
        materials.append(current_material + current_magic)
    elif result == 150:
        if "Doll" not in toys:
            toys["Doll"] = 1
        else:
            toys["Doll"] += 1
    elif result == 250:
        if "Wooden train" not in toys:
            toys["Wooden train"] = 1
        else:
            toys["Wooden train"] += 1
    elif result == 300:
        if "Teddy bear" not in toys:
            toys["Teddy bear"] = 1
        else:
            toys["Teddy bear"] += 1

    elif result == 400:
        if "Bicycle" not in toys:
            toys["Bicycle"] = 1
        else:
            toys["Bicycle"] += 1
    elif result > 0:
        materials.append(current_material + 15)

if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if 0 in magic:
    magic.remove(0)
if 0 in materials:
    materials.remove(0)
if len(materials) > 0:
    print("Materials left: ", end="")
    print(*reversed(materials), sep=", ")
if len(magic) > 0:
    print(f"Magic left: ", end="")
    print(*magic, sep=", ")

for toy, num in sorted(toys.items()):
    print(f'{toy}: {num}')
