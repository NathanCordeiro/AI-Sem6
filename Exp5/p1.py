# Water Jug Problem

# Input capacities and initial/final states
a = int(input("Enter the capacity of Jug A: "))
b = int(input("Enter the capacity of Jug B: "))
ai = int(input("Enter the initial water in Jug A: "))  # Changes every time
bi = int(input("Enter the initial water in Jug B: "))
bf = int(input("Enter the final capacity of Jug B: "))
af = int(input("Enter the final capacity of Jug A: "))

# Display available operations
print("\nList of operations you can perform:")
print("Op1: Fill Jug A completely")
print("Op2: Fill Jug B completely")
print("Op3: Empty Jug A completely")
print("Op4: Empty Jug B completely")
print("Op5: Pour water from Jug A to B until it is full")
print("Op6: Pour water from Jug B to A until it is full")
print("Op7: Pour all the water from Jug A to B")
print("Op8: Pour all the water from Jug B to A")

# Loop until the final states are reached
while ai != af or bi != bf:
    op = int(input("\nEnter the operation number: "))

    if op == 1:
        ai = a
    elif op == 2:
        bi = b
    elif op == 3:
        ai = 0
    elif op == 4:
        bi = 0
    elif op == 5:
        if (b - bi > ai):
            bi += ai
            ai = 0
        else:
            ai -= (b - bi)
            bi = b
    elif op == 6:
        if (a - ai > bi):
            ai += bi
            bi = 0
        else:
            bi -= (a - ai)
            ai = a
    elif op == 7:
        bi += ai
        ai = 0
    elif op == 8:
        ai += bi
        bi = 0

    print("Jug A:", ai, "\tJug B:", bi)
