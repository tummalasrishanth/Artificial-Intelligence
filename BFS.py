from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        v = queue.popleft()
        if v not in visited:
            print(v, end=" ")
            visited.add(v)
            queue.extend(n for n in graph[v] if n not in visited)

graph = {'A': ['B','C'], 'B': ['D','E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
bfs(graph, 'A')
