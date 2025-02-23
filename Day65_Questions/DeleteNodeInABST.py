# Question Link:- https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []

# Solution 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeft(self, root):
        while root.left is not None:
            root = root.left
        return root

    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        lastLeft = self.findLeft(root.right)
        lastLeft.left = root.left

        return root.right

    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return self.helper(root)

        dummy = root
        while dummy is not None:
            if dummy.val > key:
                if dummy.left and dummy.left.val == key:
                    dummy.left = self.helper(dummy.left)
                    break
                else:
                    dummy = dummy.left
            else:
                if dummy.right and dummy.right.val == key:
                    dummy.right = self.helper(dummy.right)
                    break
                else:
                    dummy = dummy.right

        return root 
        