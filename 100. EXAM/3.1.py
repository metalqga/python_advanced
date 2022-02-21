def print_out(flowers,birds,trees):

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
    return ""


def start_spring(**kwargs):
    flowers=[]
    birds=[]
    trees=[]

    for item,category in kwargs.items():
        if category=="flower":
            flowers.append(item)

        elif category=="bird":
            birds.append(item)

        elif category=="tree":
            trees.append(item)


    return print_out(flowers,birds,trees)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


rose="rose"
tulip="tulip"
lotus="lotus"
daffodil="daffodil"