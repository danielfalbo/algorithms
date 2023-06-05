"""
Let n be a positive integer, and let A be a list of positive integers.
We say that the integer n can be factorized by A if there exists a sequence
of integers i_1, i_2, ..., i_k (with 0 <= i_j < len(A), for j = 1, ..., k)
such that n is the product of the integers A[i_1], A[i_2], ..., A[i_k].
The following is an efficient algorithm that returns True if n can be
factorized by A, and False otherwise.
"""


# O(n * |A|)
def factorizable(n, A):
    factorizables = {0} | set(A)
    for i in range(1, n + 1):
        for a in A:
            if (i % a == 0) and (i // a) in factorizables:
                factorizables.add(i)
    return n in factorizables


if __name__ == "__main__":
    assert factorizable(6, [4, 2, 3])
    assert factorizable(8, [2, 5])
    assert not factorizable(13, [1, 2, 3, 5, 7])
    assert factorizable(0, [])
    print("all tests successful")
