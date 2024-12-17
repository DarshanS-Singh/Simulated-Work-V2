# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Problem Link:- https://leetcode.com/problems/permutation-sequence/

# Solution class
class Solution:
    def getPermutation(self, n, k):
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
    
        k -= 1
        numbers = list(range(1, n + 1))
        permutation = []

        for i in range(n, 0, -1):
            index = k // factorials[i - 1]
            k %= factorials[i - 1]
            permutation.append(numbers[index])
            numbers.pop(index)
    
        return ''.join(map(str, permutation))
    

# My Submission :- https://leetcode.com/problems/permutation-sequence/submissions/1370887891/ 