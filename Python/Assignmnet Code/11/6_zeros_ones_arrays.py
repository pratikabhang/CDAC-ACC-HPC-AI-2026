import numpy as np

def create_arrays():
    return np.zeros(10, dtype=int), np.ones(10, dtype=int)

zeros, ones = create_arrays()
print("Zeros:", zeros)
print("Ones:", ones)