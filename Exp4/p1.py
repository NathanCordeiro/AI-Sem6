graph = [
    ['A', 'B', 1, 3],
    ['A', 'C', 2, 4],
    ['A', 'H', 7, 0],
    ['B', 'D', 4, 2],
    ['B', 'E', 6, 6],
    ['D', 'H', 5, 0],
    ['D', 'E', 7, 6],
    ['C', 'F', 3, 3],
    ['C', 'G', 2, 1],
    ['F', 'H', 1, 0],
    ['G', 'H', 2, 0]
]

start = input("Enter the start node: ").strip().upper()
goal = input("Enter the goal node: ").strip().upper()

temp = []
temp1 = []

for i in graph:
    temp.append(i[0])
    temp1.append(i[1])

nodes = set(temp).union(set(temp1))

heuristic = {}
cost = {}
path = {}
open_set = set()
close_set = set()

for node in graph:
    heuristic[node[1]] = node[3]

for i in nodes:
    cost[i] = float('inf')
    path[i] = ''

open_set.add(start)
cost[start] = 0
path[start] = start

def Astar(graph, open_set, close_set, cost, currnode):
    if currnode in open_set:
        open_set.remove(currnode)

    close_set.add(currnode)

    for i in graph:
        if i[0] == currnode and (cost[i[0]] + i[2] + i[3]) < cost[i[1]]:
            open_set.add(i[1])
            cost[i[1]] = cost[i[0]] + i[2] + i[3]
            path[i[1]] = path[i[0]] + '->' + i[1]

    cost[currnode] = float('inf')
    smallest = min(cost, key=cost.get)

    if smallest not in close_set:
        Astar(graph, open_set, close_set, cost, smallest)

Astar(graph, open_set, close_set, cost, start)

print("Path is:", path[goal])

points = path[goal].split('->')
final_cost = cost[goal]

for i in points:
    if i not in [goal, start]:
        final_cost -= heuristic[i]

print("The cost of the path is:", final_cost)
