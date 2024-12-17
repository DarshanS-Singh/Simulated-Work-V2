# Question Link:- https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

# Solution Class
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        sorted_list = []
        while node:
            sorted_list.append(node.val)
            node = node.next
        sorted_list.sort()
        node = head
        for val in sorted_list:
            node.val = val
            node = node.next

        return head