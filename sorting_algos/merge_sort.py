# Merge K Sorted Linked Lists
# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:

# Input: lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]
# Example 2:

# Input: lists = []

# Output: []
# Example 3:

# Input: lists = [[]]

# Output: []
# Constraints:

# 0 <= lists.length <= 1000
# 0 <= lists[i].length <= 100
# -1000 <= lists[i][j] <= 1000

# Definition for singly-linked list.
from typing import List, Optional

# Iterative solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merges k sorted linked lists and returns it as one sorted linked list."""

        if not lists:
            return None

        index_to_heads = self.index_to_heads(lists)
        result = []
        loop = True

        while loop:
            i, lowest = self.find_lowest_node(index_to_heads)

            result.append(lowest.val)
            index_to_heads[i] = lowest.next
            loop = self.continue_loop(index_to_heads)

        return result

    def index_to_heads(self, lists: Optional[ListNode]) -> dict:
        """Returns a dict whose keys represent the index of the
        linkedlist in the lists array and whose values represent
        the current node of the linkedList.
        """

        if not lists:
            return {}

        heads = {}
        for i, head in enumerate(lists):
            heads[i] = head
        return heads

    def find_lowest_node(self, index_to_heads: dict):
        """Returns the index and node of the lowest node in the
        index_to_heads dict.
        """

        index_of_lowest = None
        lowest = None
        for index in index_to_heads:
            node = index_to_heads[index]
            if node is None:
                continue

            if lowest is None or (index is not None and node.val < lowest.val):
                lowest = node
                index_of_lowest = index
        return index_of_lowest, lowest

    def continue_loop(self, index_to_heads: dict) -> bool:
        """Returns True if a value in the index_to_heads dict is not None."""

        for index in index_to_heads:
            if index_to_heads[index] is not None:
                return True
        return False


# Test cases
# list1 = ListNode(1, ListNode(4, ListNode(5)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# list3 = ListNode(2, ListNode(6))
# lists = [list1, list2, list3]
# solution = IterativeSolution()
# merged_list = solution.mergeKLists(lists)
# print(merged_list)  # Expected output: [1,1,2,3,4,4,5,6]


# MergeSort Solution
class MergeSortSolution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merges k sorted linked lists and returns it as one sorted linked list."""

        if not lists:
            return None

        lists = [node for node in lists if node is not None]

        dummy = ListNode(0)
        current = dummy

        while lists:
            # refactored solution:
            smallest_index = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[smallest_index].val:
                    smallest_index = i
            
            # first solution:
            # smallest_node = None
            # i_of_smallest = None
            # for i, node in enumerate(lists):
            #     if node is not None:
            #         if smallest_node is None or node.val < smallest_node.val:
            #             smallest_node = node
            #             i_of_smallest = i

            current.next = lists[smallest_index]
            current = current.next

            lists[smallest_index] = lists[smallest_index].next
            if lists[smallest_index] is None:
                lists.pop(smallest_index)

        return dummy.next

    def handle_merge_sort(self, list: List[Optional[ListNode]]) -> List[ListNode]:
        """Helper function that recursively splits the list into halves
        and returns the sorted list.
        """

        if not list:
            return None

        if len(list) == 1:
            return list

        mid = len(list) // 2
        left = self.handle_merge_sort(list[:mid])
        right = self.handle_merge_sort(list[mid:])
        return self.merge_sort(left, right)

    def merge_sort(self, listA: list, listB: list) -> List[ListNode]:
        """Merges two sorted linked lists and returns it as one sorted linked list."""

        if not listA:
            return listB
        if not listB:
            return listA

        sorted = []
        a, b = 0, 0
        while a < len(listA) and b < len(listB):
            if listA[a].val < listB[b].val:
                sorted.append(listA[a])
                a += 1
            else:
                sorted.append(listB[b])
                b += 1

        sorted.extend(listA[a:])
        sorted.extend(listB[b:])

        return sorted


# Test cases
# nodeA, nodeB, nodeC, nodeD, nodeE = ListNode(
#     1), ListNode(4), ListNode(5), ListNode(1), ListNode(3)

# list_1 = [nodeA, nodeB, nodeC]
# list_2 = [nodeD, nodeE]  # Expected output:
# s = MergeSortSolution()
# result = s.merge_sort(list_1, list_2)
# print(result)  # Expected output: [1,1,3,4,5]

# Test merge_k_lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]
solution = MergeSortSolution()
merged_list = solution.merge_k_lists(lists)
# Expected output: 1,1,2,3,4,4,5,6
