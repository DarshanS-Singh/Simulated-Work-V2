# Question Link:- https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return
        rows, cols = len(matrix), len(matrix[0])
        copy_matrix = [row[:] for row in matrix]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for k in range(cols):
                        copy_matrix[row][k] = 0
                    for k in range(rows):
                        copy_matrix[k][col] = 0
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = copy_matrix[row][col]