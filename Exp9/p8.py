import numpy as np

def activation(f):
    return 1 if f >= 3.5 else 0

def neuron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def ANDgate(x):
    w = np.array([1, 1, 1])
    b = 0.5
    return neuron(x, w, b)

# Test cases
example1 = np.array([0, 0, 0])
example2 = np.array([0, 0, 1])
example3 = np.array([0, 1, 0])
example4 = np.array([0, 1, 1])
example5 = np.array([1, 0, 0])
example6 = np.array([1, 0, 1])
example7 = np.array([1, 1, 0])
example8 = np.array([1, 1, 1])

print("AND(0,0,0):", ANDgate(example1))
print("AND(0,0,1):", ANDgate(example2))
print("AND(0,1,0):", ANDgate(example3))
print("AND(0,1,1):", ANDgate(example4))
print("AND(1,0,0):", ANDgate(example5))
print("AND(1,0,1):", ANDgate(example6))
print("AND(1,1,0):", ANDgate(example7))
print("AND(1,1,1):", ANDgate(example8))
