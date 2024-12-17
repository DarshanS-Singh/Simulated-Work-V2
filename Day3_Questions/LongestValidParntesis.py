# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring.

# Question link:- https://leetcode.com/problems/longest-valid-parentheses/description/

# Solution Class

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len