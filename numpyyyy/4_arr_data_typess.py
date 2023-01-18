import numpy as np


print("data type")
d_type = np.array([1, 2, 3])
print(d_type.dtype)  # object data type
str_ar = np.array(["a", "bghyg", "c", "dfe"])
print(str_ar.dtype)
print("Creating Arrays With a Defined Data Type")
def_data = np.array([1, 23, 5, 21, 144, 46], dtype='S')
print(def_data)
print(def_data.dtype)

"""
The astype() function creates a copy of the array, 
and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. 
or you can use the data type directly like float for float and int for integer.
"""
print("Converting Data Type on Existing Arrays")
convert = np.array([1.2, 3.4, 6.9])
print(convert)
print(convert.dtype)
x = convert.astype(int)
print(x)
print(x.dtype)
s = x.astype('S')
print(s)
print(s.dtype)
print("\n")
