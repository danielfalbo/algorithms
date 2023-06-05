"""
Let v be an array of n non-negative integers. We say that v is 3-increasing
if there exist 3 indices 0 <= i < j < k <= n-1 such that v[i] < v[j] < v[k].
The following is an efficient algorithm that returns True if v is 3-increasing,
and False otherwise.
"""


# O(n)
def three_increasing(v):
    """
    args:
        v: list[int]

    returns:
        t: bool
            whether v is 3-increasing or not
    """
    s = smallest_until(v)
    l = largest_from(v)
    for i in range(1, len(v) - 1):
        if s[i] < v[i] and l[i] > v[i]:
            return True
    return False


# O(n)
def smallest_until(v):
    """
    args:
        v: list[int]

    returns:
        s: list[int]
            array such that s[i] is the smallest item in v[:i + 1]
    """
    s = v.copy()
    for i in range(1, len(v)):
        s[i] = min(s[i - 1], v[i])
    return s


# O(n)
def largest_from(v):
    """
    args:
        v: list[int]

    returns:
        l: list[int]
            array such that l[i] is the largest item in v[i:]
    """
    l = v.copy()
    for i in reversed(range(0, len(v) - 1)):
        l[i] = max(l[i + 1], v[i])
    return l


if __name__ == "__main__":
    assert three_increasing([5, 2, 1, 7, 0, 9])
    assert not three_increasing([5, 2, 1, 7, 0])
    assert three_increasing([1, 10, 20, 50, 100])
    print("all tests successful")
