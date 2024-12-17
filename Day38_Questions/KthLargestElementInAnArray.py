# Question Link:- https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Solution Class
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_numbers_min_heap = []

        for i in range(k):
            k_numbers_min_heap.append(nums[i])
        heapq.heapify(k_numbers_min_heap)

        for i in range(k, len(nums)):
            if nums[i] > k_numbers_min_heap[0]:
                heapq.heappop(k_numbers_min_heap)
                heapq.heappush(k_numbers_min_heap, nums[i])

        return k_numbers_min_heap[0]