"""
Weighted Interval Scheduling (WIS) is a generalization of
Interval Scheduling (`interval_scheduling.py`) where each
interval has a certain weight.

Interval Scheduling is the special case of WIS in which
all weights are equal to 1.

WIS is the problem of finding a subset of non-overlapping
intervals of maximum value (sum of weights).

Dynamic Programming
https://www.wikiwand.com/en/Dynamic_programming
"""

from heapsort import heapsorted as sorted
from bisect import bisect_right


START, END, WEIGHT = 0, 1, 2


class WIS:
    """
    Weighted Interval Scheduling
    """

    def __init__(self, tasks):
        """
        arguments:
            tasks: list of tasks in the tuple format (start, finish, weight)
                e.g. [(s0, f0, w0), (s1, f1, w1), (s2, f2, w2)]

        computes:
            self.__tasks: tasks sorted by finishing time
            self.__lcidx_mem: self._latest_compatible_idx(i) for all i
            self.__opt_sol_val_mem: self._opt_sol_value(i) for all i
        """

        self.__tasks = sorted(tasks, key=lambda task: task[END])

        # TODO: do this in O(n)
        # O(n log n)
        self.__lcidx_mem = {0: None}
        for j in range(1, len(tasks)):
            self.__lcidx_mem[j] = bisect_right(
                self.__tasks,
                self.__tasks[j][START],
                hi=j,
                key=lambda task: task[END]
            ) - 1
            if self.__lcidx_mem[j] < 0:
                self.__lcidx_mem[j] = None

        # O(n)
        self.__opt_sol_val_mem = {None: 0, 0: self.__tasks[0][WEIGHT]}
        for j in range(1, len(tasks)):
            jth_task_weight = self.__tasks[j][WEIGHT]
            self.__opt_sol_val_mem[j] = max(
                jth_task_weight + self.__opt_sol_val_mem[self.__lcidx_mem[j]],
                self.__opt_sol_val_mem[j-1]
            )

        self.optimal_schedule_value = self.__opt_sol_val_mem[len(tasks) - 1]

        self.__optimal_schedule_set_mem = None

    def _latest_compatible_idx(self, j):
        """
        arguments:
            j: index of a task in self.__tasks

        returns:
            i: index of latest task preceding and compatible with j
                None if no such task exists
        """
        return self.__lcidx_mem[j]

    def _opt_sol_value(self, j):
        """
        arguments:
            j: index of a task in self.__tasks

        returns:
            val: sum of weights of optimal solution considering
                    from tasks[0] up to and incuding tasks[j]
        """
        return self.__opt_sol_val_mem[j]

    def optimal_schedule_set(self):
        """
        returns:
            s: subset of non-overlapping tasks of maximum value
        """
        if self.__optimal_schedule_set_mem is None:
            s = []

            # O(n)
            i = len(self.__tasks) - 1
            while i is not None and i >= 0:
                ith_task = self.__tasks[i]
                if self._opt_sol_value(i) == ith_task[WEIGHT] + self._opt_sol_value(self._latest_compatible_idx(i)):
                    s.append(ith_task)
                    i = self._latest_compatible_idx(i)
                else:  # opt_sol_value(i) == opt_sol_value(i - 1)
                    i -= 1

            self.__optimal_schedule_set_mem = list(reversed(s))

        return self.__optimal_schedule_set_mem


if __name__ == "__main__":
    # task 0: |-----|                                   (0, 10)
    # task 1:   |---------|                             (2, 14)
    # task 2:          |--------|                       (12, 16)
    # task 3:     |-------------------|                 (6, 19)
    # task 4:                     |---------|           (17, 20)
    # task 5:                      |--------------|     (18, 24)
    #         0    10    14    16    19    20    24
    tasks = [(0, 10, 1), (2, 14, 1), (12, 16, 1),
             (6, 19, 1), (17, 20, 1), (18, 24, 1)]
    wis = WIS(tasks)
    assert wis._latest_compatible_idx(0) is None
    assert wis._latest_compatible_idx(1) is None
    assert wis._latest_compatible_idx(2) == 0
    assert wis._latest_compatible_idx(3) is None
    assert wis._latest_compatible_idx(4) == 2
    assert wis._latest_compatible_idx(5) == 2

    #   |-1-| |-1-|         |-1-| |-1-|         |-1-| |-1-|         |-1-| |-1-|
    # |------2------|     |------2------|     |------2------|     |------2------|
    # 0            10    14            20    24            30    34            40
    tasks = [
        (0, 10, 2),
        (14, 20, 2),
        (24, 30, 2),
        (34, 40, 2),
        (2, 3, 1),
        (5, 7, 1),
        (15, 16, 1),
        (17, 19, 1),
        (25, 26, 1),
        (27, 28, 1),
        (35, 36, 1),
        (37, 39, 1)
    ]

    wis = WIS(tasks)

    assert wis._opt_sol_value(0) == 1
    assert wis._opt_sol_value(1) == 2
    assert wis._opt_sol_value(2) == 2
    assert wis._opt_sol_value(3) == 3
    assert wis._opt_sol_value(4) == 4
    assert wis._opt_sol_value(5) == 4
    assert wis._opt_sol_value(6) == 5
    assert wis._opt_sol_value(7) == 6
    assert wis._opt_sol_value(8) == 6
    assert wis._opt_sol_value(9) == 7
    assert wis._opt_sol_value(10) == 8

    assert (
        wis.optimal_schedule_value
        == wis._opt_sol_value(11)
        == sum(task[WEIGHT] for task in wis.optimal_schedule_set())
        == 8
    )

    print(f"schedule: {wis.optimal_schedule_set()}")
    print(f"value: {wis.optimal_schedule_value}")

    print("all tests successful")
