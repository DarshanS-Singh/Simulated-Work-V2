# Question Link:- https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Solution Class
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False        