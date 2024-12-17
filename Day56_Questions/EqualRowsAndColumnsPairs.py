# Question Link:- https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

# Solution 
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d_rows={}
        d_columns={}
        matches=0

        for row in grid:
            h=hash(tuple(row)) 
            d_rows[h]=d_rows.get(h,0) +1

        n = len(grid)  
        columns = [[] for _ in range(n)]  

        for row in grid:
            for j in range(n): columns[j].append(row[j]) 
       
        for column in columns: 
            h=hash(tuple(column))
            d_columns[h]=d_columns.get(h,0) +1

        for h in d_rows:
            if (h in d_columns):
                print(d_rows.get(h), d_columns.get(h))
                matches += d_rows[h] * d_columns[h]

        return matches