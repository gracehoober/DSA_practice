# Write the code for a min-heap in Python
class Heap:
    def __init__(self, min_heap=True):
        self.heap = []
        self.min_heap = min_heap

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index-1) // 2


class MinHeap(Heap):
    pass


class MaxHeap(Heap):
    def __init__(self):
        super().__init__(min_heap=False)
