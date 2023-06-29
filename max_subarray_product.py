"""
Let V be an array containing n positive floating point numbers.
If i, j are two integers such that 0 <= i <= j <= n - 1,
the (i, j)-product p_(i,j) of V equals

p_(i, j) = V[i] * V[i + 1] * ... * V[j].

The following is an efficient algorithm that returns the value of one of the
largest p_(i, j) products, for 0 <= i <= j <= n - 1.
"""


def max_subarray_product(arr):
    """
    args:
        arr: list of positive floats
    returns:
        p: largest subarray product of arr
    """
    n = len(arr)

    # m[i] will be the max subarray product containing arr[i]
    m = [None for _ in range(n)]
    m[0] = arr[0]

    mx = m[0]
    for i in range(1, n):
        m[i] = max(m[i - 1] * arr[i], arr[i])
        if m[i] > mx:
            mx = m[i]
    return mx


if __name__ == "__main__":
    assert max_subarray_product([1.5, 4.0, 2.0, 0.1]) == 12.0
    assert max_subarray_product([2.0, 0.1, 2.0]) == 2.0
    assert max_subarray_product([10.0, 0.5, 4.0]) == 20.0
    assert max_subarray_product([0.2]) == 0.2
    print("all tests successful")
