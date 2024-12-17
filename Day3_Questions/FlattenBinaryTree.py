# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

#Question Link:- https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Solution Class

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        current = root
        while current is not None:

            if current.left is not None:
                last = current.left
                while last.right is not None:
                    last = last.right

                last.right = current.right
                current.right = current.left
                current.left = None

            current = current.right