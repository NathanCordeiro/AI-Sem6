graph = {
    'A': [('B', 7), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 8), ('G', 2)],
    'D': [],
    'E': [('H', 0)],
    'F': [('H', 0)],
    'G': [('H', 0)],
    'H': []
}

start = input("Enter the start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

def bfs(start, goal, graph):
    Open = [(start, 0)]
    Close = []

    while Open:
        Open.sort(key=lambda x: x[1])
        node = Open.pop(0)
        current = node[0]

        if current == goal:
            print(current)
            return

        if current not in Close:
            print(current)
            Close.append(current)

            for x in graph[current]:
                if x[0] not in [i[0] for i in Open]:
                    Open.append(x)

bfs(start, goal, graph)
