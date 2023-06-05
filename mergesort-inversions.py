"""
Merge sort
https://www.wikiwand.com/en/Merge_sort

Inversion (discrete mathematics)
https://www.wikiwand.com/en/Inversion_(discrete_mathematics)
"""


def inversions(arr):
    _, result = sorted_inversions(arr)
    return result


def mergesorted(arr):
    result, _ = sorted_inversions(arr)
    return result


# O(n log n)
def sorted_inversions(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0
    else:
        sorted_l, inversions_l = sorted_inversions(arr[: n // 2])
        sorted_r, inversions_r = sorted_inversions(arr[n // 2 :])

        sorted_arr, inversions_merge = merge_inversions(sorted_l, sorted_r)
        return sorted_arr, inversions_l + inversions_r + inversions_merge


# O(n)
def merge_inversions(l, r):
    arr = []
    inversions = 0

    i_l, i_r = 0, 0
    while i_l < len(l) and i_r < len(r):
        if r[i_r] < l[i_l]:
            inversions += 1
            arr.append(r[i_r])
            i_r += 1
        else:
            arr.append(l[i_l])
            i_l += 1

    for i in range(i_l, len(l)):
        arr.append(l[i])

    for i in range(i_r, len(r)):
        arr.append(r[i])

    return arr, inversions


if __name__ == "__main__":
    assert inversions([5, 7, 6]) == 1
    assert inversions([2, 4, 9]) == 0
    assert inversions([7, 6, 3]) == 3

    arr = [-1, 3, 10, 99, 0, 0, 0, -42]
    assert mergesorted(arr) == sorted(arr)

    assert mergesorted([]) == []

    from random import randint
    from sys import maxsize

    RANDOM_TESTS_COUNT = 100
    MAX_RANDOM_ARR_LEN = 1000

    for _ in range(RANDOM_TESTS_COUNT):
        v = [
            randint(-maxsize - 1, maxsize)
            for _ in range(randint(1, MAX_RANDOM_ARR_LEN))
        ]

        assert mergesorted(v) == sorted(v)

    print("all tests successful")
