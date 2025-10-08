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
        if not self.heap:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        priority = self.heap.pop()
        self.order_heap_pop(0)

        return priority

    def order_heap_pop(self, i=0):
        least = i
        l_i = self.left_child_i(i)
        r_i = self.right_child_i(i)

        if r_i >= len(self.heap) or l_i >= len(self.heap):
            return None

        if self.heap[l_i] < self.heap[i]:
            least = l_i
        if self.heap[r_i] < self.heap[least]:
            least = r_i

        if least != i:
            self.heap[i], self.heap[least] = self.heap[least], self.heap[i]
            self.order_heap_pop(least)
        else:
            return None

    def order_heap_push(self, i, parent_i):
        if i == 0:
            return self.heap

        if self.heap[i] < self.heap[parent_i]:
            self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
            val_i = parent_i
            parent_i = self.parent_i(val_i)
            self.order_heap_push(val_i, parent_i)

        return self.heap


class MaxHeap(Heap):
    def __init__(self):
        super().__init__(min_heap=False)


# testing


min_heap = MinHeap()
min_heap.push(5)
# min_heap.push(3)
# min_heap.push(8)
# min_heap.push(1)
# min_heap.push(7)
# min_heap.push(9)
# min_heap.push(2)

# This should pop 1
x = min_heap.pop()
print(f"Popped: {x}")
print(f"Heap after pop: {min_heap.heap}")  # [2,3,8,5,7,9]
