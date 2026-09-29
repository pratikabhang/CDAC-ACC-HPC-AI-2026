import numpy as np

def calculate_sums():
    matrix = np.arange(1, 10).reshape(3, 3)
    return matrix, matrix.sum(axis=1), matrix.sum(axis=0)

matrix, row_sum, column_sum = calculate_sums()
print(matrix)
print("Row sums:", row_sum)
print("Column sums:", column_sum)