"""
Heapsort
https://www.wikiwand.com/en/Heapsort
"""


from heap import Heap


def heapsorted(arr, reverse=False, key=lambda item: item):
    n = len(arr)

    h = Heap(max_size=n, key=key)

    for i in range(n):
        h.insert(name=i, value=arr[i])

    result = [h.pop() for _ in range(n)]

    if reverse:
        result.reverse()

    return [value for value, _ in result]


if __name__ == "__main__":
    arr = [-1, 3, 10, 99, 0, 0, 0, -42]
    assert heapsorted(arr) == sorted(arr)
    assert heapsorted([]) == []

    ########################################################
    def _key(task): return task[1]

    arr = [(0, 14), (16, 18), (0, 14), (10, 20)]
    print(f"heapsorted: {heapsorted(arr, key=_key)}")
    print(f"sorted: {sorted(arr, key=_key)}")
    assert heapsorted(arr, key=_key) == sorted(arr, key=_key)

    arr = [(0, 40), (5, 12), (15, 17), (19, 25), (35, 38)]
    assert heapsorted(arr, key=_key) == sorted(arr, key=_key)

    arr = [(0, 14), (16, 20), (10, 18)]
    assert heapsorted(arr, key=_key) == sorted(arr, key=_key)

    arr = [
        (0, 10), (20, 40), (45, 60), (65, 75),
        (5, 25), (30, 50), (55, 70),
        (5, 25), (55, 70),
        (5, 25), (55, 70)
    ]
    assert heapsorted(arr, key=_key) == sorted(arr, key=_key)

    print("all tests successful")
