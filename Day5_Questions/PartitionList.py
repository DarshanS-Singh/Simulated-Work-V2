# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

#QuestionLink:- https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150

# Solution Class

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        before,after = ListNode(0),ListNode(0)
        beforeCurr,afterCurr = before,after
        while head:
            if head.val < x:
                beforeCurr.next,beforeCurr = head, head
            else:
                afterCurr.next,afterCurr = head,head
            head = head.next
        afterCurr.next = None
        beforeCurr.next = after.next
        return before.next 