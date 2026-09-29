import numpy as np

def create_matrix():
    matrix = np.arange(1, 10).reshape(3, 3)
    return matrix

matrix = create_matrix()
print(matrix)
for row in matrix:
    print("Row:", row)
for column in matrix.T:
    print("Column:", column)