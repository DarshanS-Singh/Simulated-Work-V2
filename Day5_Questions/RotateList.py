# Given the head of a linked list, rotate the list to the right by k places

#QuestionLink:- https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150

#Solution Class

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head

        go = length - k
        first = head
        for i in range(go - 1):
            first = first.next
        nextFirst = first.next
        first.next = None
        tail = nextFirst
        while tail.next:
            tail = tail.next
        tail.next = head
        return nextFirst