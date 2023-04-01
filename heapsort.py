"""
Heapsort
https://www.wikiwand.com/en/Heapsort
"""


from heap import Heap


def heapsorted(arr):
    n = len(arr)

    h = Heap(max_size=n)

    for i in range(n):
        h.insert(key=i, value=arr[i])

    result = [h.pop() for _ in range(n)]

    return [value for value, _ in result]


if __name__ == "__main__":
    arr = [-1, 3, 10, 99, 0, 0, 0, -42]
    assert heapsorted(arr) == sorted(arr)
    assert heapsorted([]) == []
    print("all tests successful")
