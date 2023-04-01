"""
Suppose that v is an array of n elements;
v[i] is the score that student i got in the exam.

Suppose, further, that there are 3 possible scores:
    "insufficient": 0,
    "pass": 1,
    "honors": 2.

Sort v as fast as possible (in particular, beat O(n log n)).
"""


def linearly_sorted(v, domain=3):
    counts = [0 for _ in range(domain)]

    for item in v:
        assert item in range(domain)
        counts[item] += 1

    result = [None for _ in range(len(v))]

    next_idx = 0

    for domain_value in range(domain):
        for _ in range(counts[domain_value]):
            result[next_idx] = domain_value
            next_idx += 1

    assert next_idx == len(v)

    return result


if __name__ == "__main__":
    from random import randint

    RANDOM_TESTS_COUNT = 100
    MAX_RANDOM_ARR_LEN = 1000
    MAX_DOMAIN_SIZE = 100

    for _ in range(RANDOM_TESTS_COUNT):
        rand_arr_len = randint(1, MAX_RANDOM_ARR_LEN)
        rand_arr_len = 10
        domain = randint(1, MAX_DOMAIN_SIZE)
        v = [randint(0, domain - 1) for _ in range(rand_arr_len)]
        assert linearly_sorted(v, domain=domain) == sorted(v)

    assert linearly_sorted([]) == []

    INSUFFICIENT = 0
    PASS = 1
    HONORS = 2

    for v in [
        [HONORS, HONORS, PASS],
        [PASS, PASS],
        [PASS, PASS, HONORS],
        [HONORS, PASS, PASS],
        [INSUFFICIENT, INSUFFICIENT, HONORS],
        [INSUFFICIENT, INSUFFICIENT, INSUFFICIENT, INSUFFICIENT, INSUFFICIENT]
    ]:
        assert linearly_sorted(v) == sorted(v)

    print("all tests successful")
