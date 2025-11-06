"""
B-tree of order 4
https://en.wikipedia.org/wiki/B-tree
"""

N = 4
assert N % 2 == 0

import bisect

class BTree:
    def __init__(self):
        self.vals = []
        self.children = [None for _ in range(N-1)]

    def insert(self, x):
        bisect.insort(self.vals, x)
        if len(self.vals) == N + 1:
            if self.children[0] is None:
                self.children[0] = BTree()
            self.children[0].vals = self.vals[:(N // 2)]

            if self.children[-1] is None:
                self.children[-1] = BTree()
            self.children[-1].vals = self.vals[(N // 2 + 1):]

            self.vals = [self.vals[N // 2]]

if __name__ == "__main__":
    bt = BTree()
    assert bt.vals == []
    bt.insert(59)
    assert bt.vals == [59]
    bt.insert(23)
    assert bt.vals == [23, 59]
    bt.insert(7)
    assert bt.vals == [7, 23, 59]
    bt.insert(97)
    assert bt.vals == [7, 23, 59, 97]

    bt.insert(73)
    #       [59]
    #     /      \
    # [7, 23]  [73, 97]
    assert bt.vals == [59]
    assert bt.children[0].vals == [7, 23]
    assert bt.children[-1].vals == [73, 97]

    print("all tests successful")
