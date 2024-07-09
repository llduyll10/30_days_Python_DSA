from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in range(n)]
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False

# Driver code
# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4]]
# source = 0
# destination = 5

# Output = True

# run code
validPath = Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4]], source = 0, destination = 5)

print(validPath)