import numpy as np

"""
The shape of an array is the number of elements in each dimension.
NumPy arrays have an attribute called shape that returns a tuple 
with each index having the number of corresponding elements.
"""

print("Get the Shape of an Array")
sh = np.array([[2, 3, 4], [12, 13, 45]])
print(sh)
print("shape of array sh: 2 row 3 col", sh.shape)
print("\n")

"""
By reshaping we can add or remove dimensions or 
change number of elements in each dimension.
"""
print("Reshaping arrays")
resh = np.array([1,3,5,7,9,2,4,6,8,10,11,12])
print(resh)
new_shape = resh.reshape(4,3) # 4 row, 3 col 1-D to 2-D
print("1-D to 2-D\n",new_shape)
new_3d = resh.reshape(2,3,2) # 2= no.of array, 3 row in each array and 2 col in each array  3-D array
print("1-D to 3-D\n",new_3d)

"""
You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact 
number for one of the dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.
"""
new = resh.reshape(2,2,-1)
print(new)

"""
Flattening array means converting a multidimensional array into a 1D array.
We can use reshape(-1) to do this.
"""
print("\n")
print("Flattening the arrays")
f = np.array([[1,2,3],[6,5,4]])
print(f)
print("after reshape: 2D to 1D\n",f.reshape(-1))
print("\n")
