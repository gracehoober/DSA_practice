"""Kth Largest Element in a Stream
Design a class to find the kth largest integer in a stream of values, including
duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3.
The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums): Initializes the object given an integer k and
the stream of integers nums.
int add(int val): Adds the integer val to the stream and returns the kth largest
integer in the stream.

Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add",
[7],"add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6
Constraints:

1 <= k <= 1000
0 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= val <= 1000
There will always be at least k integers in the stream when you search for the
kth integer."""

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """Int: is the index of the value to return
        Stream: a heap where the smallest valuse is at stream[0] and
        largest value is at stream[-1].
        Assumption: the given stream is already an sorted list in ascending order.
        """
        self.int = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.push(val)
        if self.stream[0] > self.stream[len(self.stream) - 1]:
            self.organize_heap(len(self.stream) - 1)

        return self.stream[-3]

    def organize_heap(self, i):
        if i <= 0:
            return None

        self.stream[0], self.stream[i] = self.stream[i], self.stream[0]

        parent = i // 2
        if self.stream[i] < self.stream[parent]:
            self.organize_heap(parent)

        return None
