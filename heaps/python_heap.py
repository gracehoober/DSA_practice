class Heap:
    def __init__(self, min_heap=True):
        self.heap = []
        self.min_heap = min_heap

    def left_child_i(self, index):
        return 2 * index + 1

    def right_child_i(self, index):
        return 2 * index + 2

    def parent_i(self, child_i):
        return (child_i-1) // 2


class MinHeap(Heap):
    def push(self, val):
        self.heap.append(val)

        i = len(self.heap)-1
        parent_i = self.parent_i(i)
        return self.order_heap(i, parent_i)

    def order_heap(self, i, parent_i):
        if i == 0:
            return self.heap

        if self.heap[i] < self.heap[parent_i]:
            self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
            val_i = parent_i
            parent_i = self.parent_i(val_i)
            self.order_heap(val_i, parent_i)

        return self.heap


class MaxHeap(Heap):
    def __init__(self):
        super().__init__(min_heap=False)
