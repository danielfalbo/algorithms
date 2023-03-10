"""
Stable Marriage Problem
https://en.wikipedia.org/wiki/Stable_marriage_problem

Gale-Shapley algorithm
https://en.wikipedia.org/wiki/Gale-Shapley_algorithm

Related: LeetCode 1583. Count Unhappy Friends
https://leetcode.com/problems/count-unhappy-friends/
"""


def gale_shapley(n, apref, ranking):
    free = Node.range(n)
    nxt = [0 for _ in range(n)]
    current = [None for _ in range(n)]

    while free:
        a_i = free.value
        b_j = apref[a_i][nxt[a_i]]
        nxt[a_i] += 1
        if current[b_j] is None:
            current[b_j] = a_i
            free = free.nxt
        else:
            a_k = current[b_j]
            if ranking[b_j][a_i] < ranking[b_j][a_k]:
                current[b_j] = a_i
                free.value = a_k

    return current


class Node:
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def range(n):
        head = tail = Node(0, prev=None, nxt=None)
        for _ in range(n - 1):
            tail.nxt = Node(tail.value + 1, prev=tail, nxt=None)
            tail = tail.nxt
        return head


if __name__ == "__main__":
    n = 2

    apref = [[None for _ in range(n)] for _ in range(n)]

    # a0: b0 > b1
    apref[0][0] = 0
    apref[0][1] = 1

    # a1: b0 > b1
    apref[1][0] = 0
    apref[1][1] = 1

    ranking = [[None for _ in range(n)] for _ in range(n)]

    # b0: a0 > a1
    ranking[0][0] = 0
    ranking[0][1] = 1

    # b1: a0 > a1
    ranking[1][0] = 0
    ranking[1][1] = 1

    stable_match = gale_shapley(n, apref, ranking)
    assert stable_match == [0, 1]
    print({f"b{i}": f"a{stable_match[i]}" for i in range(n)})

    ########################################################
    n = 3

    apref = [[None for _ in range(n)] for _ in range(n)]

    # a0: b0 > b1 > b2
    apref[0][0] = 0
    apref[0][1] = 1
    apref[0][2] = 2

    # a1: b0 > b1 > b2
    apref[1][0] = 0
    apref[1][1] = 1
    apref[1][2] = 2

    # a2: b2 > b0 > b1
    apref[2][0] = 2
    apref[2][1] = 0
    apref[2][2] = 1

    ranking = [[None for _ in range(n)] for _ in range(n)]

    # b0: a2 > a0 > a1
    ranking[0][2] = 0
    ranking[0][0] = 1
    ranking[0][1] = 2

    # b1: a2 > a0 > a1
    ranking[1][2] = 0
    ranking[1][0] = 1
    ranking[1][1] = 2

    # b2: a2 > a0 > a1
    ranking[2][2] = 0
    ranking[2][0] = 1
    ranking[2][1] = 2

    stable_match = gale_shapley(n, apref, ranking)
    assert stable_match == [0, 1, 2]
    print({f"b{i}": f"a{stable_match[i]}" for i in range(n)})

    ########################################################
    n = 4

    apref = [[None for _ in range(n)] for _ in range(n)]

    # a0: b3 > b2 > b1 > b0
    apref[0][0] = 3
    apref[0][1] = 2
    apref[0][2] = 1
    apref[0][3] = 0

    # a1: b3 > b1 > b0 > b2
    apref[1][0] = 3
    apref[1][1] = 1
    apref[1][2] = 0
    apref[1][3] = 2

    # a2: b1 > b2 > b3 > b0
    apref[2][0] = 1
    apref[2][1] = 2
    apref[2][2] = 3
    apref[2][3] = 0

    # a3: b3 > b0 > b1 > b2
    apref[3][0] = 3
    apref[3][1] = 0
    apref[3][2] = 1
    apref[3][3] = 2

    ranking = [[None for _ in range(n)] for _ in range(n)]

    # b0: a1 > a0 > a2 > a3
    ranking[0][1] = 0
    ranking[0][0] = 1
    ranking[0][2] = 2
    ranking[0][3] = 3

    # b1: a3 > a2 > a0 > a1
    ranking[1][3] = 0
    ranking[1][2] = 1
    ranking[1][0] = 2
    ranking[1][1] = 3

    # b2: a0 > a1 > a3 > a2
    ranking[2][0] = 0
    ranking[2][1] = 1
    ranking[2][3] = 2
    ranking[2][2] = 3

    # b3: a3 > a1 > a0 > a2
    ranking[3][3] = 0
    ranking[3][1] = 1
    ranking[3][0] = 2
    ranking[3][2] = 3

    stable_match = gale_shapley(n, apref, ranking)
    assert stable_match == [1, 2, 0, 3]
    print({f"b{i}": f"a{stable_match[i]}" for i in range(n)})
