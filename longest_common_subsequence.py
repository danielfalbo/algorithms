"""
Longest common substring
https://wikiwand.com/en/Longest_common_subsequence
"""


def lcss(s, t):
    """
    args:
        s: string
        t: string
    returns:
        l: length of the longest common subsequence of s and t
    """
    n, m = len(s), len(t)

    if n == 0 or m == 0:
        return 0

    # dp[i][j] will be the length of the longest common subsequence
    # of s[:i] and t[:j] (note that s[i] and t[j] are not included)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # O(n * m)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            eq = s[i - 1] == t[j - 1]
            if eq:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    assert lcss("", "") == 0
    assert lcss("a", "a") == 1
    assert lcss("ac", "ab") == 1
    assert lcss("abcde", "ace") == 3
    assert lcss("abc", "abc") == 3
    assert lcss("abc", "def") == 0
    assert lcss("serendipitous", "precipitation") == 7
    assert lcss("", "fdsajkl;") == 0
    assert lcss([1, 3, 5, 6, 7, 2, 5, 2, 3], [6, 2, 4, 7, 1, 5, 6, 2, 3]) == 5
    print("all tests successful")
