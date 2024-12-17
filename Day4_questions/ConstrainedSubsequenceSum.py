# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two 
# consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

#Problem link:- https://leetcode.com/problems/constrained-subsequence-sum/description/

# Solution Class

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        deque=[]
        for i,num in enumerate(nums):
            while deque and deque[0]<i-k:
                deque.pop(0)
            if deque:
                nums[i]=nums[deque[0]]+num
            while deque and nums[deque[-1]]<nums[i]:
                deque.pop()
            if nums[i]>0:
                deque.append(i)
        return max(nums) 