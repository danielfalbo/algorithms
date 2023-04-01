"""
Heap (data structure)
https://www.wikiwand.com/en/Heap_(data_structure)
"""


class Heap:
    """
    key-value min-heap
    (parent.value <= child.value)
    """

    def parent_idx(child_idx): return (child_idx - 1) // 2
    def left_child_idx(parent_idx): return (parent_idx * 2) + 1
    def right_child_idx(parent_idx): return Heap.left_child_idx(parent_idx) + 1

    class FullHeapException(Exception):
        def __init__(self):
            super().__init__("heap is already full")

    def __init__(self, max_size):
        self.__nodes_count = 0
        self.__allocated_size = max_size

        # self.__arr[i] will be the (value, key) tuple of the ith element of the heap
        self.__arr = [None for _ in range(max_size)]

        # self.__position[i] will be the index of the item with key i in self.__arr
        self.__position = [None for _ in range(max_size)]

    def __getitem__(self, key: int):
        if self.__nodes_count == 0:
            raise IndexError("empty heap")
        elif self.__position[key] is None:
            raise KeyError(key)
        else:
            i = self.__position[key]
            assert 0 <= i < self.__nodes_count
            return self.__arr[i]

    def get_root(self):
        if self.__nodes_count == 0:
            raise IndexError("pop from empty heap")
        else:
            return self.__arr[0]

    def __len__(self):
        return self.__nodes_count

    def __str__(self):
        return f"{self.__arr[:self.__nodes_count]}"

    def __swap(self, i, j):
        _, ith_node_key = self.__arr[i]
        _, jth_node_key = self.__arr[j]
        self.__arr[i], self.__arr[j] = self.__arr[j], self.__arr[i]
        self.__position[ith_node_key], self.__position[jth_node_key] = j, i

    def insert(self, key, value):
        if self.__nodes_count == self.__allocated_size:
            raise Heap.FullHeapException
        else:
            self.__arr[self.__nodes_count] = (value, key)
            assert self.__position[key] is None
            self.__position[key] = self.__nodes_count
            self.__heapify_up(self.__nodes_count)
            self.__nodes_count += 1

    def __heapify_up(self, index):
        child_idx, parent_idx = index, Heap.parent_idx(index)
        child, parent = self.__arr[child_idx], self.__arr[parent_idx]

        if child_idx > 0 and child < parent:
            self.__swap(child_idx, parent_idx)
            self.__heapify_up(parent_idx)

    def pop(self):
        if self.__nodes_count == 0:
            raise IndexError("pop from empty heap")
        else:
            popped_node_value, popped_node_key = self.__arr[0]

            last_node_idx = self.__nodes_count - 1
            self.__swap(0, last_node_idx)
            self.__position[popped_node_key] = None
            self.__arr[last_node_idx] = None
            self.__nodes_count -= 1

            self.__heapify_down(0)

            return (popped_node_value, popped_node_key)

    def __heapify_down(self, index):
        parent_idx = index
        left_child_idx = Heap.left_child_idx(index)
        right_child_idx = Heap.right_child_idx(index)

        if left_child_idx >= self.__nodes_count:
            # no childs
            return
        elif left_child_idx == self.__nodes_count - 1:
            # only left child
            smaller_child_idx = left_child_idx
        else:
            # both right and left child
            left_child, right_child = self.__arr[left_child_idx], self.__arr[right_child_idx]
            smaller_child_idx = left_child_idx if left_child < right_child else right_child_idx

        parent, smaller_child = self.__arr[parent_idx], self.__arr[smaller_child_idx]

        if smaller_child < parent:
            self.__swap(parent_idx, smaller_child_idx)
            self.__heapify_down(smaller_child_idx)


if __name__ == "__main__":
    h = Heap(max_size=10)
    assert len(h) == 0

    key, value = 0, 10
    h.insert(key=key, value=value)
    assert len(h) == 1
    assert h.get_root() == (value, key)

    key, value = 1, 19
    h.insert(key=key, value=value)
    assert len(h) == 2
    assert h.get_root() == (10, 0)

    key, value = 2, 1
    h.insert(key=key, value=value)
    assert len(h) == 3
    assert h.get_root() == (value, key)

    print(h)

    value, key = h.pop()
    assert value == 1 and key == 2
    assert len(h) == 2
    assert h.get_root() == (10, 0)

    h.pop()
    assert len(h) == 1
    assert h.get_root() == (19, 1)

    h.pop()
    assert len(h) == 0

    try:
        h.get_root()
        print(h.get_root())
        assert False is True
    except IndexError:
        pass

    try:
        h.pop()
        assert False is True
    except IndexError:
        pass

    assert str(h) == "[]"
    print(h)

    print("all tests successful")
