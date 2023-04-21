def bisect_right(sorted_list, value, lo=0, hi=None, key=lambda item: item):
    """
    Returns the rightmost (largest) index where to insert the item in the list,
    assuming the list is sorted.

    Optional args lo (default 0) and hi (default len(sorted_list))
    bound the slice of the list to be searched.

    Optional arg key is a lambda function used to evaluate the list items
    (and not for the passed value to insert).
    """
    if hi is None:
        hi = len(sorted_list)

    assert hi >= lo

    if lo == hi:
        return lo
    elif hi == lo + 1:
        return hi if key(sorted_list[lo]) <= value else lo
    else:
        mid = lo + ((hi - lo) // 2)
        if key(sorted_list[mid]) <= value:
            return bisect_right(sorted_list, value, lo=mid, hi=hi, key=key)
        else:
            return bisect_right(sorted_list, value, lo=lo, hi=mid, key=key)


if __name__ == "__main__":
    from bisect import bisect_right as py_bisect_right

    tests = [
        ([-12, 2, 4, 5, 11, 321], -1),
        ([], 10),
        ([1, 2, 3, 3, 3, 4, 5, 6, 7], 3)
    ]

    for l, a in tests:
        assert py_bisect_right(l, a) == bisect_right(l, a)

    l, a = [0, 0, 0, 0, 0, 0], 1
    assert py_bisect_right(l, a, lo=3, hi=3) == bisect_right(l, a, lo=3, hi=3)

    l, a = tests[2]
    assert py_bisect_right(l, a, hi=3) == bisect_right(l, a, hi=3)
    assert py_bisect_right(l, a, hi=2) == bisect_right(l, a, hi=2)
    assert py_bisect_right(l, a, hi=1) == bisect_right(l, a, hi=1)
    assert py_bisect_right(l, a, lo=1, hi=2) == bisect_right(l, a, lo=1, hi=2)
    assert (
        py_bisect_right(l, a, lo=3, hi=len(l) - 1)
        == bisect_right(l, a, lo=1, hi=len(l) - 1)
    )

    print("all tests successful")
