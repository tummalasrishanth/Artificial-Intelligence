from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    
    min_path = None
    min_cost = float('inf')
    
    for perm in permutations(vertices):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_path = path
            
    return min_path, min_cost

# Example graph represented as a distance matrix
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

path, cost = tsp(graph, 'A')
print("Shortest path:", " -> ".join(path))
print("Total cost:", cost)
