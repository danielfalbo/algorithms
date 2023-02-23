"""
Stable Marriage Problem
https://en.wikipedia.org/wiki/Stable_marriage_problem

Gale-Shapley algorithm
https://en.wikipedia.org/wiki/Gale-Shapley_algorithm

LeetCode 1583. Count Unhappy Friends
https://leetcode.com/problems/count-unhappy-friends/
"""


def gale_shapley(a, b, preferences):
    """
    Let A and B be two disjoint sets of cardinality n each
    ( A intersection B = empty set, |A| = |B| = n ).

    A perfect matching between A and B is a pairing of the
    elements of A with the elements of B.
    That is, M, subset of { {a, b} | a in A, b in B }, is a
    perfect matching iff for every a in A there exists exactly
    one b in B such that {a, b} is in M (and viceversa).

    Suppose that each a in A has a sorted preference over B,
    and that each b in B has a sorted preference list over A.

    Two distinct pairs {a, b}, {a', b'} in M exhibit an instability if
    - a prefers b' to b, and
    - b' prefers a to a'.

    M is a stable matching if it contains no instabilities.

    If I give you all the preference lists,
    1. does there exist a stable matching?
    2. how to find it, if it exists?

    With the Gale-Shapley algorithm,
    it is possible to prove 1. and do 2.

    This function implements Gale-Shapley algorithm.

    a: set of strings such that itself and b are disjoint
    b: set of strings such that itself and a are disjoint

    preferences: dictionary mapping elements of a and b to their sorted preference list
                 (the higher their index, the higher the preference)

    returns: dictionary mapping each element of a to an element of b

    e.g.
    a = {"a1", "a2"}
    b = {"b1", "b2"}

    preferences = {
        "a1": ["b2", "b1"], # a1: b1 > b2
        "a2": ["b2", "b1"], # a2: b1 > b2

        "b1": ["a2", "a1"], # b1: a1 > a2
        "b2": ["a2", "a1"] # b2: a1 > a2
    }
    """
    pairs_a_to_b = {}
    pairs_b_to_a = {}

    # while there is some free a in A that hasn't yet proposed to each b in B
    while a:
        # let a_i be a free element of A
        a_i = a.pop()
        # let best_b be the element of B' that ranks highest in a_i's preference list
        best_b = preferences[a_i].pop()
        # if b is free
        if best_b in b:
            # match a_i and best_b
            pairs_a_to_b[a_i] = best_b
            pairs_b_to_a[best_b] = a_i
            # a_i and best_b are not free anymore
            b.remove(best_b)
        else:
            current = pairs_b_to_a[best_b]
            if preferences[best_b].index(a_i) > preferences[best_b].index(current):
                # match a_i and best_b
                pairs_a_to_b[a_i] = best_b
                pairs_b_to_a[best_b] = a_i
                # "break up" {best_b, current}
                del pairs_a_to_b[current]
                a.add(current)
            else:
                # a_i remains free, and best_b remains engaged with her current partner
                a.add(a_i)

    return pairs_a_to_b


if __name__ == "__main__":
    a = {"a1", "a2"}
    b = {"b1", "b2"}

    preferences = {
        "a1": ["b2", "b1"],  # a1: b1 > b2
        "a2": ["b2", "b1"],  # a2: b1 > b2

        "b1": ["a2", "a1"],  # b1: a1 > a2
        "b2": ["a2", "a1"]  # b2: a1 > a2
    }

    stable_match = gale_shapley(a, b, preferences)
    print(stable_match)

    ########################################################

    a = {"a1", "a2", "a3"}
    b = {"b1", "b2", "b3"}

    preferences = {
        "a1": ["b3", "b2", "b1"],  # a1: b1 > b2 > b3
        "a2": ["b3", "b2", "b1"],  # a2: b1 > b2 > b3
        "a3": ["b2", "b1", "b3"],  # a3: b3 > b1 > b2


        "b1": ["a2", "a1", "a3"],  # b1: a3 > a1 > a2
        "b2": ["a2", "a1", "a3"],  # b2: a3 > a1 > a2
        "b3": ["a2", "a1", "a3"],  # b3: a3 > a1 > a2
    }

    stable_match = gale_shapley(a, b, preferences)
    print(stable_match)
