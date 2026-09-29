import numpy as np

def calculate_statistics():
    array = np.arange(1, 21)
    return array, array.sum(), array.mean(), array.max(), array.min()

array, total, mean, maximum, minimum = calculate_statistics()
print(array)
print("Sum:", total)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)