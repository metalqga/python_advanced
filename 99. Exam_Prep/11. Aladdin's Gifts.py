from collections import deque
materials = [int(x) for x in input().split()]
magic = [int(x) for x in input().split()]
magic = deque(magic)
presents = {}


def gifts(result):
    gift = None
    if 100 <= result <= 199:
        gift = "Gemstone"
    elif 200 <= result <= 299:
        gift = "Porcelain Sculpture"
    elif 300 <= result <= 399:
        gift = "Gold"
    elif 400 <= result <= 499:
        gift = "Diamond Jewellery"
    if gift not in presents and gift != None:
        presents[gift] = 1
    elif gift in presents and gift != None:
        presents[gift] += 1


def mixing(materials, magic):
    while materials and magic:
        current_material = materials.pop()
        current_magic = magic.popleft()
        result = current_magic + current_material
        if result < 100:
            if result % 2 == 0:
                result = current_material * 2 + current_magic * 3
            else:
                result = result * 2
        if result > 499:
            result = result / 2
        gifts(result)


def print_result(presents, materials, magic):
    if ("Gemstone" in presents and "Porcelain Sculpture" in presents) or (
            "Gold" in presents and "Diamond Jewellery" in presents):
        print(f"The wedding presents are made!")
    else:
        print(f"Aladdin does not have enough wedding presents.")
    materials = [str(x) for x in materials]
    magic = [str(x) for x in magic]
    if materials:
        print(f"Materials left: {', '.join(materials)}")
    if magic:
        print(f"Magic left: {', '.join(magic)}")
    if presents:
        for present, num in sorted(presents.items()):
            print(f"{present}: {num}")


mixing(materials, magic)
print_result(presents, materials, magic)