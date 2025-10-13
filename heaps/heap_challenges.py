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


"""Last Stone Weight
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]

Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]

Output: 1
Constraints:

1 <= stones.length <= 20
1 <= stones[i] <= 100"""


class LastStoneWeight:
    def __init__(self, stones):
        self.stones = stones

    def play(self):
        """Initiates the play of last stone weight and returns the larget
        remaining stone.
        """

        if not self.stones:
            return 0

        while (len(self.stones) > 1):
            self.smash()

        return self.stones[0] if self.stones else 0

    def two_heaviest(self):
        """Returns the indicies of the two largest stones in self.stones."""

        if len(self.stones) < 2:
            return None, None

        stoneA = 0
        stoneB = 1
        for i, stone in enumerate(self.stones):
            if stone > self.stones[stoneA]:
                stoneB = stoneA
                stoneA = i
            elif stone > self.stones[stoneB]:
                stoneB = i

        return stoneA, stoneB

    def smash(self):
        """Mutates the self.stones array in place by removing the smallest
        of two stones and reducing the largest of two stones by the value of
        the smallest.
        """

        stoneA, stoneB = self.two_heaviest()

        if self.stones[stoneA] == self.stones[stoneB]:
            self.stones.pop(stoneB)
            self.stones.pop(stoneA)
        elif self.stones[stoneA] < self.stones[stoneB]:
            self.stones[stoneB] = self.stones[stoneB] - self.stones[stoneA]
            self.stones.pop(stoneA)
        else:
            self.stones[stoneA] = self.stones[stoneA] - self.stones[stoneB]
            self.stones.pop(stoneB)


# Testing:
stones = [2, 3, 6, 2, 4]
last_stone_weight = LastStoneWeight(stones=stones)
stone = last_stone_weight.play()
print(stone)

"""
K Closest Points to Origin
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100"""
