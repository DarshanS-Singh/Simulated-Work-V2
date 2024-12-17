# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Solution Class
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        res=[]
        
        def backtrack(i,j):
            if (i<m and i>=0 and j<n and j>=0) and obstacleGrid[i][j]!=1:
                if (i,j)==(m-1,n-1):
                    if obstacleGrid[i][j]==1:
                        return 0
                    mat[i][j]=1
                if mat[i][j]!=-1:
                    return mat[i][j]                    
                mat[i][j]=backtrack(i+1,j)+backtrack(i,j+1)
                
            else:
                mat[i][j]=0
            return mat[i][j]
        mat=[[-1]*(n+1) for elem in range(m+1)]
        
        return backtrack(0,0)