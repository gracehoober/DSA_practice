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
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index_to_heads = self.heads(lists)
        result = []

        i, lowest = self.find_lowest_node(index_to_heads)

        result.push(lowest)
        index_to_heads[i] = lowest.next


# compare the keys/head values in heads counter
# find the largest and put into new list
# make the head.next the new head

#how to handle the case where the linkedList val is None

    def index_to_heads(listsList[Optional[ListNode]])-> dict:
        """Returns a dict whose keys represent the index of the
        linkedlist in the lists array and whose values represent
        the current node of the linkedList.
        """
        # {0:head, 1:head, 2:head}
        heads = {}
        for i,head in enumerate(lists):
            heads[i]=head
        return heads

    def find_lowest_node(index_to_heads: dict):
        i = 0
        lowest = index_to_heads
        for index in index_to_heads:
            node = index_to_heads[index]
            if node.val < lowest:
                lowest = node
                i = index
        