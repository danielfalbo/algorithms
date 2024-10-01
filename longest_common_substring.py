"""
Longest common substring
https://www.wikiwand.com/en/Longest_common_substring
"""


def lcs(s, t):
    """
    args:
        s: string
        t: string
    returns:
        l: length of the longest common substring of s and t
    """
    mx = 0
    n, m = len(s), len(t)

    if n == 0 or m == 0:
        return mx

    # v[i][j] will be the longest common substring containing s[i] and t[j]
    # and, eventually, only contiguous elements to their left
    v = [[0 for _ in t] for _ in s]

    # O(n * m)
    for i in range(n):
        for j in range(m):
            lcs_with_left_neighbs = v[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            v[i][j] = 0 if s[i] != t[j] else 1 + lcs_with_left_neighbs
            if v[i][j] > mx:
                mx = v[i][j]
    return mx


if __name__ == "__main__":
    assert lcs("", "") == 0
    assert lcs("a", "a") == 1
    assert lcs("ac", "ab") == 1
    assert lcs("abcdgh", "acdghrx") == 4
    assert lcs("abcdef", "efbcd") == 3
    assert lcs("abcdaf", "zbcddf") == 3
    print("all tests successful")
