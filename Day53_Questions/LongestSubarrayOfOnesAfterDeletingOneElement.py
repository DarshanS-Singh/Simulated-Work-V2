# Question Link:- https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Solution
def longestSubarray(nums):
    vis = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            vis.append(count)
        else:
            count += 1
    if count is not 0:
        vis.append(count)
    if len(vis) == 0:
        return len(nums) - 1
    if len(vis) is 1:
        return len(nums) - 1
    max_sum = 0
    for i in range(len(vis) - 1):
        max_sum = max(max_sum, vis[i] + vis[i + 1])
    return max_sum