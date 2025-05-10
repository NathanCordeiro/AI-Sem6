graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

def dfs_shortest_path(graph, start, goal):
    open=[start]
    closed=[]
    if start == goal:
        print("\nStart is goal node")
        return open
    while open:
        path=open.pop()
        node=path[-1]
        if node not in closed:
            closed.append(node)
            neighbours=graph[node]
            
            for i in neighbours:
                new_path=list(path)
                new_path.append(i)
                open.append(new_path)
                
                if i==goal:
                    return new_path        
        
    print("Goal not found")
    return

print("Shortest path is:", dfs_shortest_path(graph, start, goal))