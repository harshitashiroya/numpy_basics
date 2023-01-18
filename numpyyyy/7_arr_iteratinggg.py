import numpy as np


"""
Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, 
we can do this using basic for loop of python.
If we iterate on a 1-D array it will go through each element one by one.
"""
print("Iterating Arrays")
i = np.array([ [[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]] ]) # 3-D aaray
print("3D array:\n", i)
print("\n")
for x in i: # 3D to 2D  print(x)
      for y in x: #2D to 1D  print(y)
            for z in y: #1D to single element
                  print(z)

print("\nIterating Arrays Using np.nditer():")


for x in np.nditer(i):
      print(x)

"""
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype 
to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) 
so it needs some other space to perform this action, that extra space is called buffer, 
and in order to enable it in nditer() we pass flags=['buffered'].
"""
print("\nchange data tytpe in iterating:")
for x in np.nditer(i, flags=['buffered'], op_dtypes=['S']):
  print(x)

print("\nIterating With Different Step Size:")
for x in np.nditer(i[:, ::2]): # array skipping 1 element
  print(x)

"""
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, 
the ndenumerate() method can be used for those usecases.
"""
print("\nEnumerated Iteration Using ndenumerate():")
for idx, x in np.ndenumerate(i):
  print(idx, x)