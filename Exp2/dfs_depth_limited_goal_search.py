graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()
limit = int(input("Enter depth limit: ").strip())

def dls(graph, start, goal, limit):
    def dls_recursive(node, goal, limit, path, visited):
        if limit < 0:
            return None
        path.append(node)
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dls_recursive(neighbor, goal, limit - 1, path, visited)
                if result:
                    return result
        path.pop()
        return None

    visited = set()
    path = []
    result = dls_recursive(start, goal, limit, path, visited)
    
    if result:
        return result
    else:
        print("\nGoal not found within depth limit")
        return []

print("Path is:", dls(graph, start, goal, limit))
