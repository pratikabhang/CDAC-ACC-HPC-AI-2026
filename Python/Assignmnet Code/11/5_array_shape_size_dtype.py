import numpy as np

def array_properties():
    array = np.array([[10, 20, 30], [40, 50, 60]])
    return array, array.shape, array.size, array.dtype

array, shape, size, dtype = array_properties()
print(array)
print("Shape:", shape)
print("Size:", size)
print("Data type:", dtype)