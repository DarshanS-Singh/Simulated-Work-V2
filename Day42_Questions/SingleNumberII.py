# Question Link:- https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# Solution Class
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            ans |= bit_sum << i
        if ans >= 2**31:
            ans -= 2**32

        return ans
        