# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
# modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


#Problem Link:- https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Solution Class

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        curr = head

        while curr and curr.next:
            temp = curr.next.next

            tail.next = curr.next
            curr.next.next = curr
            curr.next = temp

            tail = curr
            curr = temp

        return dummy.next