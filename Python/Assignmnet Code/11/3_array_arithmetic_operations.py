import numpy as np

def perform_operations():
    array = np.array([10, 20, 30, 40, 50])
    return array + 5, array - 5, array * 2, array / 2

addition, subtraction, multiplication, division = perform_operations()
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)