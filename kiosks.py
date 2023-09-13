"""
There is a country road in a park. This road has t rest areas,
the first of which positioned at km x_1, the second of which at km x_2, ...,
and the last of which positioned at km x_t (with x_1 < x_2 < ... < x_t).
The owner of the park can decide, for each rest area i, whether to open up
a kiosk in rest area i, or to avoid doing so.

For each i = 1, 2, ..., t, opening up a kiosk in the ith rest area produces
a revenue of e_i euros. Local regulations make it impossible to open two
kiosks at distance less than or equal 5 kms from each other.

The following is an efficient algorithm for finding a set of kiosks
that maximizes the total revenue of the park.
"""


def kiosks(locations, values):
    """
    args:
        locations: list of rest areas locations
        values: list of potential revenues of opening a kiosk at each location

    returns:
        r: int, best revenue possibly obtainable
    """
    assert len(locations) == len(values)
    t = len(locations)
    # mem[i] = best revenue considering locations[:i+1]
    #           with a kiosk opened at locations[i] location
    mem = [values[i] for i in range(t)]
    for i in range(1, t):
        mem[i] = values[i] + max(
            {mem[j] for j in range(i) if locations[i] - locations[j] >= 5}, default=0
        )
    return max(mem)


if __name__ == "__main__":
    assert kiosks([1, 5, 9], [1000, 1000, 1000]) == 2000
    assert kiosks([1, 5, 9], [1000, 10000, 1000]) == 10000
    assert kiosks([1, 3, 4, 6], [1000, 1000, 1000, 1000]) == 2000
    assert kiosks([1, 3, 4, 5], [1000, 1000, 1000, 1000]) == 1000
    print("all tests successful")
