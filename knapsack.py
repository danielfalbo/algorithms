"""
Knapsack Problem
https://www.wikiwand.com/en/Knapsack_problem
"""

VALUE, SIZE = 0, 1


def knapsack(items, capacity):
    """
    args:
        items: list of (value, size) items
        capacity: size of the knapsack

    returns:
        s: subset of items that fits the knapsack with max value sum
    """
    # mem[i][k] will be the best value we can get from
    # the first i items for a knapsack of capacity k
    mem = [[None for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(len(items) + 1):
        mem[i][0] = 0
    for k in range(capacity + 1):
        mem[0][k] = 0

    for i in range(1, len(items) + 1):
        ith_item_val, ith_item_size = items[i - 1]
        for smaller_capacity in range(1, capacity + 1):
            if ith_item_size > smaller_capacity:
                mem[i][smaller_capacity] = mem[i-1][smaller_capacity]
            else:
                mem[i][smaller_capacity] = max(
                    ith_item_val + mem[i-1][smaller_capacity - ith_item_size],
                    mem[i-1][smaller_capacity]
                )

    i, k = len(items), capacity
    goal_value = mem[i][k]
    s = []
    while i > 0 and k > 0 and goal_value > 0:
        if mem[i - 1][k] == goal_value:
            i -= 1
        else:
            ith_item = ith_item_val, ith_item_size = items[i - 1]
            s.append(ith_item)
            i -= 1
            k -= ith_item_size
            goal_value -= ith_item_val
    return s


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

    order = knapsack(menu, calorie_budget)
    assert sum(map(lambda item: item[SIZE], order)) <= calorie_budget
    assert sum(map(lambda item: item[VALUE], order)) == 359

    print("all tests successful")
