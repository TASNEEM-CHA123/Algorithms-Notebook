from collections import deque

# ********************* BLACKBOX STARTS *********************
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, src, dest):
        # directed edge
        self.adj[src].append(dest)

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        visited[start] = True
        queue.append(start)

        result = []  # store traversal

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result
        
# ********************* BLACKBOX endS *********************
# create graph object
g = Graph(4)

# add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# run BFS
result = g.bfs(2)

print("BFS Traversal:", result)
