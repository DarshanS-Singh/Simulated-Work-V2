#Question Link:- https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150

# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Solution Class
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        list_length = len(nums1)
        min_heap = []
        pairs = []

        for i in range(min(k, list_length)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        counter = 1
        while min_heap and counter <= k:
            sum_of_pairs, i, j = heappop(min_heap)

            pairs.append([nums1[i], nums2[j]])

            next_element = j + 1
            if len(nums2) > next_element:
                heappush(min_heap, (nums1[i] + nums2[next_element], i, next_element))

            counter += 1
        return pairs