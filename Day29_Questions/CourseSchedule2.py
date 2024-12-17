# Question Link:- https://leetcode.com/problems/course-schedule-ii/description/?envType=study-plan-v2&envId=top-interview-150 

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

# Solution Class

class Solution(object):
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        sorted_order = []
        if n <= 0:
            return sorted_order
        in_degree = {i: 0 for i in range(n)}
        graph = {i: [] for i in range(n)}

        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[0]
            graph[parent].append(child)
            in_degree[child] += 1  

        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(sorted_order) != n:
            return []

        return sorted_order