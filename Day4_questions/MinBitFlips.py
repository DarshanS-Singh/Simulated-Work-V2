# You are given a binary array nums and an integer k.

# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

# A subarray is a contiguous part of an array.

# problem Link:- https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/

# Solution class

class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums)
        flipCountOffset= [0]* n
        flips = 0
        ans = 0
        
        for i in range(n):
            flips+= flipCountOffset[i]
            num = nums[i]^1 if flips % 2 else nums[i]
            nums[i] =  num
            # print(nums)
            
            if num == 0:
                if i+k > n:
                    return -1
                
                nums[i] ^= 1
                if i+k < n:
                    flipCountOffset[i+k]-=1
                flips+=1
                ans+=1 
                
        return ans