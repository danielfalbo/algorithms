"""
Interval Scheduling Problem (`interval_scheduling.py`):
what's the max number of requests a single resource can handle?

Interval Partitioning Problem:
what's the min number of resources needed to handle all requests?

Also see Algorithm Design book by Jon Kleinberg and Éva Tardos
"""

from heapsort import heapsorted as sorted


def partition(tasks):
    """
    args:
        tasks: list of tasks
                e.g. [(s0, f0), (s0, f0), (s1, f1)]

    returns:
        tasks: reordered list of tasks

        resources: list such that
                    resources[i] == n means ith task is assigned to nth resource
    """
    resources = [None for _ in range(len(tasks))]
    next_resource = 1

    tasks = sorted(tasks, key=lambda task: task[0])

    for j in range(len(tasks)):
        l = set(range(1, next_resource + 1))

        for i in range(j):
            assert tasks[j][0] >= tasks[i][0]

            if not compatible(tasks[i], tasks[j]):
                l -= {resources[i]}

        assert len(l) >= 1
        resources[j] = l.pop()

        if resources[j] == next_resource:
            next_resource += 1

    return tasks, resources


def compatible(task1, task2):
    s1, t1 = task1[0], task1[1]
    s2, t2 = task2[0], task2[1]

    # one of the two tasks starts after the other ended
    return s2 > t1 or s1 > t2


if __name__ == "__main__":

    # helper function to make testing easier
    def compatible_partitioning(tasks, l):
        """
        args:
            tasks: list of tasks
                    e.g. [(s0, f0), (s0, f0), (s1, f1)]

            l: list such that l[i] == n means tasks[i] is assigned to nth resource

        returns: True if for each resource all its tasks are compatible, False otherwise
        """
        d = max(l)
        for resource in range(1, d + 1):
            resource_tasks = [tasks[i]
                              for i in range(len(tasks))
                              if l[i] == resource]

            for i in range(len(resource_tasks)):
                for j in range(i):
                    if not compatible(resource_tasks[i], resource_tasks[j]):
                        return False
        return True

    ########################################################

    #       |-----------------------|
    # |-----------|     |-----|
    # |-----------|
    # 0    10    14    16    18    20
    tasks = [
        (10, 20),
        (0, 14), (16, 18),
        (0, 14),
    ]
    tasks, l = partition(tasks)
    d = max(l)
    assert d == 3
    assert compatible_partitioning(tasks, l)
    print(f"depth: {d}")
    [print(f"resource {l[i]} runs {tasks[i]}") for i in range(len(tasks))]

    ########################################################
    print()

    #    |-----|     |-----|    |-----|      |---|
    # |--------------------------------------------|
    # 0    10    14    16    18    20   30        40
    tasks = [
        (5, 12), (15, 17), (19, 25), (35, 38),
        (0, 40)
    ]
    tasks, l = partition(tasks)
    d = max(l)
    assert d == 2
    assert compatible_partitioning(tasks, l)
    print(f"depth: {d}")
    [print(f"resource {l[i]} runs {tasks[i]}") for i in range(len(tasks))]

    ########################################################
    print()

    # |-----------|    |------------|
    #       |----------------|
    # 0    10    14   16    18     20
    tasks = [
        (0, 14), (16, 20),
        (10, 18)
    ]
    tasks, l = partition(tasks)
    d = max(l)
    assert d == 2
    assert compatible_partitioning(tasks, l)
    print(f"depth: {d}")
    [print(f"resource {l[i]} runs {tasks[i]}") for i in range(len(tasks))]

    ########################################################
    print()

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
    tasks, l = partition(tasks)
    d = max(l)
    assert d == 4
    assert compatible_partitioning(tasks, l)
    print(f"depth: {d}")
    [print(f"resource {l[i]} runs {tasks[i]}") for i in range(len(tasks))]
