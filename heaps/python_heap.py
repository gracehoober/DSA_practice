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
        return self.order_heap_push(i, parent_i)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.order_heap_pop(0)

        return self.heap.pop()

    def order_heap_pop(self, i):
        least = i
        l_i = self.left_child_i(i)
        r_i = self.right_child_i(i)

        if r_i >= len(self.heap) or l_i >= len(self.heap):
            return

        if self.heap[l_i] < self.heap[i]:
            least = l_i
        if self.heap[r_i] < least:
            least = r_i

        if least is not i:
            self.heap[i], self.heap[least] = self.heap[least], self.heap[i]
            self.order_heap_pop(least)
        else:
            return

    def order_heap_push(self, i, parent_i):
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


# testing
min_heap = MinHeap()
min_heap.push(1)
min_heap.push(2)
min_heap.push(4)
min_heap.push(3)
x = min_heap.pop()
len = min_heap.heap
print(len)
