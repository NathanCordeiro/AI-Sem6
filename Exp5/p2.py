# Water Jug Problem (Three Jugs)

# Input capacities and goal states
x = int(input("Enter the maximum capacity of Jug A: "))
y = int(input("Enter the maximum capacity of Jug B: "))
z = int(input("Enter the maximum capacity of Jug C: "))
goalx = int(input("Enter the goal state in Jug A: "))
goaly = int(input("Enter the goal state in Jug B: "))

# Dictionary to mark visited states
visited = {}  
# List to store solution path
path = []  

def all_states(state):
    jugA, jugB, jugC = state

    if jugA == goalx and jugB == goaly:
        path.append(state)
        return True

    if state in visited:
        return False

    visited[state] = 1

    # Pouring water from Jug A
    if jugA > 0:
        if jugA + jugB <= y:
            if all_states((0, jugA + jugB, jugC)):
                path.append(state)
                return True
        else:
            if all_states((jugA - (y - jugB), y, jugC)):
                path.append(state)
                return True

        if jugA + jugC <= z:
            if all_states((0, jugB, jugA + jugC)):
                path.append(state)
                return True
        else:
            if all_states((jugA - (z - jugC), jugB, z)):
                path.append(state)
                return True

    # Pouring water from Jug B
    if jugB > 0:
        if jugA + jugB <= x:
            if all_states((jugA + jugB, 0, jugC)):
                path.append(state)
                return True
        else:
            if all_states((x, jugB - (x - jugA), jugC)):
                path.append(state)
                return True

        if jugB + jugC <= z:
            if all_states((jugA, 0, jugB + jugC)):
                path.append(state)
                return True
        else:
            if all_states((jugA, jugB - (z - jugC), z)):
                path.append(state)
                return True

    # Pouring water from Jug C
    if jugC > 0:
        if jugA + jugC <= x:
            if all_states((jugA + jugC, jugB, 0)):
                path.append(state)
                return True
        else:
            if all_states((x, jugB, jugC - (x - jugA))):
                path.append(state)
                return True

        if jugB + jugC <= y:
            if all_states((jugA, jugB + jugC, 0)):
                path.append(state)
                return True
        else:
            if all_states((jugA, y, jugC - (y - jugB))):
                path.append(state)
                return True

    return False

# Initialize the first state
initial_state = (x, 0, 0)

print("Starting work...\n")
all_states(initial_state)

# Reverse the path to display the correct sequence
path.reverse()

# Print the solution path
for state in path:
    print(state)
