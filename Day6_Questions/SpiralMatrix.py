# Given an m x n matrix, return all elements of the matrix in spiral order.

# Question Link:- https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

# Solution class

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1
        result = []
        while rows > 0 and cols > 0:
            for _ in range(cols):
                col += direction
                result.append(matrix[row][col])
            rows -= 1
            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1
            direction *= -1
        return result  