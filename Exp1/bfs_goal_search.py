graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []
}

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

def bfs_goal_search(graph, start, goal):
    closed = []
    open = [start]
   
    if start == goal:
        print("Start node is the goal node")
        return [start]
   
    closed.append(start)

    while open:
        node = open.pop(0)
        neighbors = graph[node]
        for i in neighbors:
            if i not in closed:
                closed.append(i)
                open.append(i)
                if i == goal:
                    return closed
    print("Goal not found")
   

print("Traversal is:", bfs_goal_search(graph, start, goal))