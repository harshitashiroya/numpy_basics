import numpy as np


"""
NumPy Array Indexing
The indexes in NumPy arrays start with 0, 
meaning that the first element has index 0, and the second has index 1 etc.
"""
print("index in 1-D array")
index_1D = np.array([23, 45, 678, 43, 760])
print("value at index 1:", index_1D[1])
print("\n")

"""
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers 
representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, 
where the dimension represents the row and the index represents the column.
"""
print("index in 2D array")
index_2D = np.array([[1, 2], [3, 4]])
print(index_2D)
print("value at 1st row and 2nd column:", index_2D[0, 1])

index_2D2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(index_2D2)
print('5th element on 2nd row: ', index_2D2[1, 4])
print("\n")
"""
Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated 
integers representing the dimensions and the index of the element.
"""
print("index in 3-D array ")
index_3D = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
#                                 0                                1
#                          0            1                    0               1
#                       0, 1, 2, 3    0, 1, 2, 3       0, 1, 2, 3       0, 1, 2, 3
# negative index       -4,-3,-2,-1   -4,-3,-2,-1      -4,-3,-2,-1       -4,-3,-2,-1
print(index_3D)
print(index_3D[1, 1, 3])

print("negative index")
print(index_3D[1, 1, -1])
print("\n")
