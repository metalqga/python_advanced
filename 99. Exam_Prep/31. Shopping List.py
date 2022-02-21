def shopping_list(budget, **kwargs):
    text = ""
    if budget < 100:
        return "You do not have enough budget."

    else:
        counter = 0
        for arg in kwargs:
            price, quantity = (kwargs.get(arg))
            result = price * quantity
            if result <= budget:
                budget -= result
                text += (f"You bought {arg} for {result:.2f} leva.")
                counter += 1
                if counter >= 5:
                    break
                if budget <= 0:
                    break
                text+="\n"

    return text


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(2, 4),
                    coffee=(1.50, 10),
                    ))
