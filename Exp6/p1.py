graph = {
    'A': [('B', 3), ('C', 4), ('K', 10)],
    'B': [('D', 1), ('E', 0)],
    'C': [('F', 2), ('G', 3)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'K': []
}

start = input("Enter the Start Node: ").strip().upper()
goal = input("Enter the Goal Node: ").strip().upper()

def hill_climb(start, goal, graph):
    open_list = []
    close_list = []

    open_list.append(start)
    
    while open_list:
        node = open_list.pop(0)

        if node == goal:
            print("Goal found")
            close_list.append(node)
            print(close_list)
            return True

        close_list.append(node)
        neighbors = graph[node]

        for neighbor in neighbors:
            if neighbor[0] not in open_list:
                open_list.append(neighbor[0])
                break

    print("Goal not found")

hill_climb(start, goal, graph)
