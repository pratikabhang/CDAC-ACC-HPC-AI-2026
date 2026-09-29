import numpy as np

def array_operations():
    first = np.array([1, 2, 3, 4, 5])
    second = np.array([10, 20, 30, 40, 50])
    return first + second, first * second

addition, multiplication = array_operations()
print("Addition:", addition)
print("Multiplication:", multiplication)