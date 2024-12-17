# Question link:- https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# Solution 

def isSubsequence(s,t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == j[t]:
            i += 1
        j += 1
    return i == len(s)