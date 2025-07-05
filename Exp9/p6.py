import numpy as np

def activation(f):
    return 1 if f >= 0 else 0

def neuron1(x, w1, b1):
    r1 = np.dot(x, w1) + b1
    return activation(r1)

def neuron2(x, w2, b2):
    r2 = np.dot(x, w2) + b2
    return activation(r2)  

def neuron3(r1, r2, w3, b3):
    inputs = np.array([r1, r2])
    r3 = np.dot(inputs, w3) + b3
    return activation(r3)    

def XORgate(x):
    w1 = np.array([-1, -1])
    b1 = 1.5
    r1 = neuron1(x, w1, b1)

    w2 = np.array([-1, -1])
    b2 = 0.5
    r2 = neuron2(x, w2, b2)

    w3 = np.array([1, -1])
    b3 = -0.5
    r3 = neuron3(r1, r2, w3, b3)

    return r3

# Test cases
example1 = np.array([0, 0])
example2 = np.array([0, 1])
example3 = np.array([1, 0])
example4 = np.array([1, 1])

print("XOR(0,0):", XORgate(example1))
print("XOR(0,1):", XORgate(example2))
print("XOR(1,0):", XORgate(example3))
print("XOR(1,1):", XORgate(example4))
