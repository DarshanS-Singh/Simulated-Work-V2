#Question Link:- https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorde

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderidx = {v : i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            
            root = TreeNode(postorder.pop())

            idx = inorderidx[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)
            return root
        
        return helper(0, len(inorder) - 1)