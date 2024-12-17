# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Problem link:- https://leetcode.com/problems/combination-sum-ii/ 

class Solution:
    def __init__(self):
        self.result = [] 
    def solve(self, nums, target, index, lst):
        if target == 0:
            self.result.append(lst[:]) 
            return
        if index == len(nums) or target < nums[index]:
            return
        temp = nums[index]
        lst.append(nums[index]) 
        self.solve(nums, target - nums[index], index + 1, lst)
        lst.pop() 
        i = 1
        while index + i < len(nums) and nums[index + i] == temp:
            i += 1
        self.solve(nums, target, index + i, lst)
    def combinationSum2(self, candidates, target):
        candidates.sort()  
        self.solve(candidates, target, 0, [])  
        return self.result  