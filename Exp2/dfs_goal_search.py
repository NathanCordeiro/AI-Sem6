graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

def dfs_goal_search(graph, start, goal):
    visited = []
    stack = [start]
    
    if start == goal:
        print("Start node is the goal node")
        return [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            neighbors = graph[node]
            for i in neighbors:
                if i not in visited:
                    stack.append(i)
    print("Goal not found")
    return 

print("Traversal is:", dfs_goal_search(graph, start, goal))
