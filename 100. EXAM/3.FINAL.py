def start_spring(**kwargs):
    new_dict = {}
    result = ""
    for item, category in kwargs.items():
        if category not in new_dict:
            new_dict[category] = [item]
        else:
            new_dict[category].append(item)
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for category, items in sorted_dict.items():
        result += (f"{category}:\n")
        for item in sorted(items):
            result += (f"-{item}\n")
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
