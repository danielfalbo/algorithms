"""
Interval Scheduling Problem
https://en.wikipedia.org/wiki/Interval_scheduling

Greedy algorithm
https://en.wikipedia.org/wiki/Greedy_algorithm

Earliest Deadline First (EDF) scheduling
https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling

Related:
        LeetCode 621. Task Scheduler
        https://leetcode.com/problems/task-scheduler/

        LeetCode 646. Maximum Length of Pair Chain
        https://leetcode.com/problems/maximum-length-of-pair-chain/description/

        LeetCode 1520. Maximum Number of Non-Overlapping Substrings
        https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/
"""


def edf(tasks):
    """
    arguments:
        tasks: list of tasks
            e.g. [(s0, t0), (s0, t0), (s1, t1)]

    returns:
        s: biggest set of non-overlapping tasks
    """
    t = float("-inf")  # last finishing time
    s = set()  # result

    tasks.sort(key=lambda task: task[1])

    for i in range(len(tasks)):
        if tasks[i][0] > t:
            s.add(tasks[i])
            t = tasks[i][1]

    return s


if __name__ == "__main__":
    #       |-----------------------|
    # |-----------|     |-----|
    # |-----------|
    # 0    10    14    16    18    20
    tasks = [(0, 14), (0, 14), (10, 20), (16, 18)]
    biggest_schedule_set = edf(tasks)
    assert biggest_schedule_set == {(0, 14), (16, 18)}
    print(edf(tasks))

    ########################################################

    #    |-----|     |-----|    |-----|      |---|
    # |--------------------------------------------|
    # 0    10    14    16    18    20   30        40
    tasks = [(0, 40), (5, 12), (15, 17), (19, 25), (35, 38)]
    biggest_schedule_set = edf(tasks)
    assert biggest_schedule_set == {(5, 12), (15, 17), (19, 25), (35, 38)}
    print(edf(tasks))

    ########################################################

    # |-----------|    |------------|
    #       |----------------|
    # 0    10    14   16    18     20
    tasks = [(0, 14), (16, 20), (10, 18)]
    biggest_schedule_set = edf(tasks)
    assert biggest_schedule_set == {(0, 14), (16, 20)}
    print(edf(tasks))

    ########################################################

    # |-----------|    |-------------|   |------------|    |---------|
    #        |--------------|    |-----------|    |------------|
    #        |--------------|                     |------------|
    #        |--------------|                     |------------|
    # 0      5   10   20   25   30  40  45  50   55  60   65  70    75
    tasks = [
        (0, 10), (20, 40), (45, 60), (65, 75),
        (5, 25), (30, 50), (55, 70),
        (5, 25), (55, 70),
        (5, 25), (55, 70)
    ]
    biggest_schedule_set = edf(tasks)
    assert biggest_schedule_set == {(0, 10), (20, 40), (45, 60), (65, 75)}
    print(edf(tasks))
