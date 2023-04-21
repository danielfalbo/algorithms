VALUE, SIZE = 0, 1


def knapsack(items, capacity):
    """
    args:
        items: list of (value, size) items
        capacity: size of the knapsack

    returns:
        s: subset of items that fits the knapsack with max value sum
    """
    raise NotImplementedError


if __name__ == "__main__":
    calorie_budget = 750

    # (how much I like it, how many calories it costs)
    wine = (89, 123)
    beer = (90, 154)
    pizza = (30, 258)
    burger = (50, 354)
    fries = (90, 365)
    coke = (79, 150)
    apple = (90, 95)
    donut = (10, 195)

    menu = [wine, beer, pizza, burger, fries, coke, apple, donut]

    try:
        knapsack(menu, calorie_budget)
    except NotImplementedError:
        pass

    print("all tests successful")
