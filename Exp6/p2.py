graph = {
    'A': [('B', 3), ('C', 4), ('K', 10)],
    'B': [('D', 1), ('E', 0)],
    'C': [('F', 2), ('G', 3)],
    'D': [], 'E': [], 'F': [], 'G': []
}

heuristics = {
    'A': 5, 'B': 3, 'C': 4, 'K': 10, 'D': 1, 'E': 0, 'F': 2, 'G': 3
}

def steepest(start, goal):
    current = start

    while True:
        print("Current Node:", current)

        if current == goal:
            print("Goal found!")
            return

        neighbors = graph.get(current, [])
        if not neighbors:
            print("Stuck at local maxima")
            return

        neighbors.sort(key=lambda x: heuristics[x[0]])
        best_neighbor, _ = neighbors[0]  # Ignoring heuristic value for readability
        current = best_neighbor

# Get user input for start and goal nodes
start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

steepest(start, goal)
