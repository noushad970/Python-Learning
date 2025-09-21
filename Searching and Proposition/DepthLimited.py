def dls(graph, start, goal, limit, path=None):
    if path is None:
        path = []
    
    path.append(start)
    print("Visiting:", start)

    if start == goal:
        return path
    
    if limit <= 0:   # depth limit reached
        path.pop()
        return None
    
    for neighbor in graph[start]:
        if neighbor not in path:   # avoid cycles
            result = dls(graph, neighbor, goal, limit - 1, path)
            if result:
                return result
    
    path.pop()
    return None


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Depth Limited Search:")
result = dls(graph, 'A', 'F', 2)   # depth limit = 2
print("Result Path:", result)
