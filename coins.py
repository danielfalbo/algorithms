"""
In a country there are three types of coin: the first has value a,
the second has value b, and the thirs has value c. In the country,
a price w can be paid exactly if and only if there exist three non-negative
integers i_a, i_b, and i_c such that w = i_a * a + i_b * b + i_c * c
—that is, such that w equals the total value of i_a coins of value a,
i_b coins of value b, and i_c coins of value c. The following is an
algorithm that, given a, b, c, and a price w, returns True if w can be
paid exactly, and False otherwise.
"""


def payable(a, b, c, w):
    """
    args:
        a: int
            positive integer, value of coin a
        b: int
            positive integer, value of coin b
        c: int
            positive integer, value of coin c

        w: int
            non-negative integer, price to be paid

    returns:
        p: bool
            whether w can be paid exactly with coins of values a, b, and c
    """
    m = {0}

    # O(w)
    for i in range(1, w + 1):
        if (i - a) in m or (i - b) in m or (i - c) in m:
            m.add(i)

    return w in m


if __name__ == "__main__":
    assert payable(1, 5, 7, 13)
    assert not payable(2, 4, 8, 7)
    print("all tests successful")
