import numpy as np

"""
-> Getting some elements out of an existing array and creating 
a new array out of them is called filtering.

-> In NumPy, you filter an array using a boolean index list.

-> A boolean index list is a list of booleans corresponding to indexes in the array.

-> If the value at an index is True that element is contained in the filtered array, 
if the value at that index is False that element is excluded from the filtered array.
"""

fil_array = np.array([1,3,6,89,90])
#                     F,T,T, F, T
x = [False,True,True,False,True]

z = fil_array[x]

print(z)


ar = np.array([1,4,7,9,10,8])
fi_arr = []

for i in ar:
    if i > 5:
        fi_arr.append(True)
    else:
        fi_arr.append(False)

new_array = ar[fi_arr]
print(fi_arr)
print(new_array)
print("\n")

print("Creating Filter Directly From Array")
filter_arr = ar % 4 == 0
new_fil_array = ar[filter_arr]
print(new_fil_array)
print(filter_arr)