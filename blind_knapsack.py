"""
Knapsack Problem but you're blind.

You can't identify items and their values but only their size,
so you only aim at filling the knapsack as much as you can.

https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/subsetsum.pdf
"""


def blind_knapsack(items, capacity):
    """
    args:
        items: list of sizes of available items
        capacity: size of the knapsack

    returns:
        s: list, subset of items that fills the knapsack the most
    """
    n = len(items)

    # mem[n][capacity] = blind_knapsack(items[:n], capacity)
    mem = [
        [None for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]
    # 0 items cases
    for smaller_capacity in range(capacity + 1):
        mem[0][smaller_capacity] = 0
    # capacity == 0 cases
    for i in range(n + 1):
        mem[i][0] = 0

    for i in range(1, n + 1):
        ith_item = items[i - 1]

        for smaller_capacity in range(1, capacity + 1):
            if smaller_capacity < ith_item:
                mem[i][smaller_capacity] = mem[i-1][smaller_capacity]
            elif smaller_capacity >= ith_item:
                mem[i][smaller_capacity] = max(
                    mem[i-1][smaller_capacity],
                    ith_item + mem[i-1][smaller_capacity-ith_item]
                )

    i = n
    j = capacity
    goal_value = mem[i][j]
    knapsack = []
    while i > 0 and j > 0:
        if mem[i - 1][j] == goal_value:
            i -= 1
        else:
            ith_item = items[i-1]
            knapsack.append(ith_item)
            i -= 1
            j -= ith_item

    return knapsack


if __name__ == "__main__":
    jobs_durations = [3, 3, 5]

    available_time = 5
    knapsack = blind_knapsack(jobs_durations, available_time)
    value = sum(knapsack)
    print(f"knapsack: {knapsack}")
    print(f"value: {value}")
    assert value == 5

    available_time = 6
    knapsack = blind_knapsack(jobs_durations, available_time)
    value = sum(knapsack)
    print(f"knapsack: {knapsack}")
    print(f"value: {value}")
    assert value == 6

    available_time = 4
    knapsack = blind_knapsack(jobs_durations, available_time)
    value = sum(knapsack)
    print(f"knapsack: {knapsack}")
    print(f"value: {value}")
    assert value == 3

    print("all tests successful")
