def ids(graph, start, goal, max_depth):
    def dls(node, goal, limit, path):
        path.append(node)
        if node == goal:
            return path
        if limit <= 0:
            path.pop()
            return None
        for neighbor in graph[node]:
            if neighbor not in path:
                result = dls(neighbor, goal, limit - 1, path)
                if result:
                    return result
        path.pop()
        return None

    for depth in range(max_depth + 1):
        result = dls(start, goal, depth, [])
        if result:
            return result
    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(ids(graph, 'A', 'F', 3))
