colours = input().split()
main_colours = ["red", "yellow", "blue"]
secondary_colours = ["orange", "purple", "green"]
found = []

while len(colours) > 0:
    first = colours[0]
    second = colours[-1]
    temp_colour1 = first + second
    temp_colour2 = second + first

    if temp_colour1 in main_colours or temp_colour1 in secondary_colours:
        colours.remove(colours[0])
        colours.remove(colours[-1])
        found.append(temp_colour1)

    elif temp_colour2 in main_colours or temp_colour2 in secondary_colours:
        colours.remove(colours[0])
        colours.remove(colours[-1])
        found.append(temp_colour2)

    elif len(colours)==1:
        temp_colour1=colours[0]
        if temp_colour1 in main_colours or temp_colour1 in secondary_colours:
            colours.remove(colours[0])
            found.append(temp_colour1)
            break
        else:
            break

    else:
        colours.remove(first)
        if len(colours) >= 1:
            colours.remove(second)
        if len(first[:(len(first) - 1)])>0:
            colours.insert(len(colours) // 2, first[:(len(first) - 1)])
        if len(second[:(len(second) - 1)])>0:
            colours.insert(len(colours) // 2, second[:(len(second) - 1)])

if "orange" in found:
    if "red" not in found or "yellow" not in found:
        found.remove("orange")
if "purple" in found:
    if "red" not in found or "blue" not in found:
        found.remove("purple")
if "green" in found:
    if "yellow" not in found or "blue" not in found:
        found.remove("green")
print(found)
