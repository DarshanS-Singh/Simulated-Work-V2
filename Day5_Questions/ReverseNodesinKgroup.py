# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

#Question Link:- https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150

# Solution Class

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, tail):
            prev, curr = None, head
            while curr != tail:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        while head:
            tail = prev_tail
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nextHead = tail.next
            newHead = reverse(head, tail.next)
            prev_tail.next = newHead
            head.next = nextHead
            prev_tail = head
            head = nextHead

        return dummy.next
