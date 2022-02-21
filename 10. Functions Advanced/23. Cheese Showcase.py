def sorting_cheeses(**kwargs):
    sorted_cheeses=sorted(kwargs.items(), key=lambda kvpt:(-len(kvpt[1]),kvpt[0]))
    result=''

    for name, size in sorted_cheeses:
        result+=name +"\n"
        size=sorted(size, reverse=True)
        for element in size:
            result+=str(element) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)