graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []
}

start = input("Enter start node: ").strip().upper()
limit = int(input("Enter depth limit: ").strip())

def dls(graph, start, limit):
    def dls_recursive(node, limit, path, visited):
        if limit < 0:
            return
        path.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dls_recursive(neighbor, limit - 1, path, visited)
        path.pop()

    visited = set()
    path = []
    dls_recursive(start, limit, path, visited)
    return visited

print("Nodes visited within depth limit:", dls(graph, start, limit))
