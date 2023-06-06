"""
Maximum Product Cutting problem
Integer Break problem

Given a positive integer n, a "cutting" of n is a sequence of positive integers
a1, a2, ..., ak that sum up to n, that is, such that \sum_{i = 1}^{k} a_i = n.
The value of a sequence a1, a2, ..., ak is equal to the product of its terms
a1 * a2 * ••• * ak. The following is an efficient algorithm that, given an
integer n >= 2, returns the value of a cutting of n of maximum value.
"""


# O(n^2)
def cutting(n):
    assert n >= 2
    m = [j for j in range(n + 1)]  # m[j] = value of best cutting of j
    for j in range(2, n + 1):
        for i in range(1, j):
            if i * m[j - i] > m[j]:
                m[j] = i * m[j - i]
    return m[n]


if __name__ == "__main__":
    assert cutting(2) == 2
    assert cutting(7) == 12
    assert cutting(9) == 27
    print("all tests successful")
