def start_spring(**kwargs):
    flowers=[]
    birds=[]
    trees=[]
    insects=[]

    for item,category in kwargs.items():
        if category=="flower":
            flowers.append(item)

        elif category=="bird":
            birds.append(item)

        elif category=="tree":
            trees.append(item)

        elif category=="insect":
            insects.append(item)

    if flowers:
        print("flower: ")
        for flower in sorted(flowers):
            print(f"-{flower}")
    if birds:
        print("bird: ")
        for bird in sorted(birds):
            print(f"-{bird}")
    if trees:
        print("tree: ")
        for tree in sorted(trees):
            print(f"-{tree}")
    if insects:
        print("insect: ")
        for insect in sorted(insects):
            print(f"-{insect}")
    return

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


