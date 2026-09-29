import numpy as np

def marks_statistics():
    marks = np.array([78, 85, 92, 67, 88])
    return marks, marks.max(), marks.min(), marks.mean()

marks, highest, lowest, average = marks_statistics()
print("Marks:", marks)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)