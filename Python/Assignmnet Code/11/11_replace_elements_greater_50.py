import numpy as np

def replace_values():
    array = np.array([10, 55, 30, 70, 45, 90])
    array[array > 50] = 0
    return array

print(replace_values())