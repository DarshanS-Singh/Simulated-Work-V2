# Question Link https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Solution Class

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        min_heap = []
        
        for list_node in lists:
            if list_node:
                heapq.heappush(min_heap, (list_node.val, id(list_node), list_node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            _, _, smallest_node = heapq.heappop(min_heap)
            current.next = smallest_node  
            current = current.next  

            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, id(smallest_node.next), smallest_node.next))

        return dummy.next  