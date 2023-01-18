"""
NumPy is a Python library.
NumPy is used for working with arrays.
NumPy is short for "Numerical Python".
"""
"""
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.
"""

import numpy as np

a = np.array([1, 2, 3, 4])  # create an array
print(a)
print(type(a))  # type of variable
print(a.dtype)  # type of data stored in variable

print(np.__version__)  # numpy version
print("\n")
"""
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
and it will be converted into an ndarray:
"""

b = np.array((2, 4, 6, 8))
print(b)
print(type(b))
print("\n")

"""
ndim -> to check dimension
"""
# zero dimension array

ze = np.array(40)
print(ze)
print("zero:", ze.ndim)
print("\n")

# 1-D array

one = np.array([1, 2, 3, 4])
print(one)
print("one: ", one.ndim)
print("\n")

# 2-D array

two = np.array([[1, 2], [3, 4]])
print(two)
print("two:", two.ndim)
print("\n")

# 3-D array

three = np.array([[[1, 2, 3], [3, 4, 5], [5, 6, 7]]])
print(three)
print("three:", three.ndim)
print("\n")

"""
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions 
by using the ndmin argument.
"""
new_arr = np.array([1, 2, 3, 4], ndmin=10)
print(new_arr)
print('number of dimensions :', new_arr.ndim)
print("\n")



