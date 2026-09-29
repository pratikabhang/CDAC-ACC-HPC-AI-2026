import numpy as np

def sort_array():
    array = np.array([45, 12, 78, 23, 56, 9])
    ascending = np.sort(array)
    descending = np.sort(array)[::-1]
    return ascending, descending

ascending, descending = sort_array()
print("Ascending:", ascending)
print("Descending:", descending)