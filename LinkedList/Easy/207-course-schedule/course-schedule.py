
from collections import deque
class Solution(object):
    def canFinish(self,numCourses, prerequisites):
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses
            




        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        