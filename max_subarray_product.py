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
        mx: largest subarray product of arr
    """
    mx = arr[0]
    acc = mx
    for i in range(1, len(arr)):
        if arr[i] > 1.0:
            acc *= arr[i]
            if acc > mx:
                mx = acc
        else:
            acc = 1.0
    return mx


if __name__ == "__main__":
    assert max_subarray_product([1.5, 4.0, 2.0, 0.1]) == 12.0
    assert max_subarray_product([2.0, 0.1, 2.0]) == 2.0
    print("all tests successful")
