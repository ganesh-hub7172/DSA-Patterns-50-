class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False  # cycle found
            if visited[course] == 2:
                return True   # already processed

            visited[course] = 1  # mark visiting

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            visited[course] = 2  # mark done
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
