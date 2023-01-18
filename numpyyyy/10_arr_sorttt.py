import numpy as np

"""
-> Sorting means putting elements in an ordered sequence.
-> Ordered sequence is any sequence that has an order corresponding to elements, 
like numeric or alphabetical, ascending or descending.
-> The NumPy ndarray object has a function called sort(), that will sort a specified array.
"""

s_array = np.array([1,4,7,3,67,34,12,87])
print(s_array)

x = np.sort(s_array)
print("after sorting: ",x) # This method returns a copy of the array, leaving the original array unchanged.


str = np.array(["hello","harshita","shiroya"])
print(np.sort(str))

bool_val = np.array([True,False,False,True])
print(np.sort(bool_val))

array_2d = np.array([[1,9,2],[90,10,7]])
print(np.sort(array_2d))