"""
Consider a rectilinear road of t kilometers.

Among the road there are k houses,
the i_th of which at km d_i on the road.

    🏠      🏠          🏠     🏠
|---|-------|-----------|------|----|
   d1      d2    ...   d3     dk    t km

A GSM company wants to build antennas so to
cover each house with its network.

Given that an antenna covers a radius
of 10 KMs, what is the smallest number of antennas
that have to be built?
"""

from heapsort import heapsorted as sorted


def antennas(houses, radius):
    """
    args:
        houses: list
                such that houses[i] == d means that
                the i_th house is located at the d_th kilometer

        radius: int, radius covered by an antenna

    returns:
        locations: list
                    such that locations[i] == d means that
                    the i_th antenna should be placed at the d_th kilometer
    """
    locations = []

    houses = sorted(houses, reverse=True)

    while houses:
        # place antenna at first uncovered house location + radius
        antenna = houses.pop() + radius
        locations.append(antenna)

        # remove all houses now covered by the new antenna
        i = antenna - radius
        j = antenna + radius
        house = len(houses) - 1
        while house >= 0 and i <= houses[house] <= j:
            house -= 1
            houses.pop()

    return locations


if __name__ == "__main__":
    #      🏠    🏠                         🏠
    #      [           📡           ]       [      📡      ]
    # |----|-----|-----|------------|-------|------|-------|
    # 0    3     9    13           23      30     40      50
    houses = [9, 3, 30]
    locations = antennas(houses, radius=10)
    assert locations == [13, 40]
    print(f"{len(locations)} antennas, placed at kilometers {locations}")

    ##################################################

    #      🏠    🏠         🏠   🏠        🏠                  🏠
    #      [           📡             ]    [     📡     ]      [     📡    ]
    # |----|-----|-----|----|----|----|----|-----|------|------|-----|-----|
    # 0    3     8    13   15   19   23   26    36     46    100   110   120
    houses = [3, 26, 19, 8, 15, 100]
    locations = antennas(houses, radius=10)
    assert locations == [13, 36, 110]
    print(f"{len(locations)} antennas, placed at kilometers {locations}")
