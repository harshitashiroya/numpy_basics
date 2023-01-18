import numpy as np

"""
Joining means putting contents of two or more arrays in a single array.

We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. 
If axis is not explicitly passed, it is taken as 0.
"""
print("..........array join...........\n")
print("Joining 1D Arrays:")

ar1 = np.array([12,23,45])
print("array-1: ",ar1)

ar2 = np.array([15,78,90])
print("array 2: ", ar2)

join_array = np.concatenate((ar1,ar2))
print("after joining: ", join_array)

print("\n")
print("Joining 2D Arrays:")

ar1_2d = np.array([[1,2],[3,4]])
print("array -1:\n",ar1_2d)

ar2_2d = np.array([[5,6],[8,9]])
print("array 2:\n",ar2_2d)

join_2d_array = np.concatenate((ar1_2d,ar2_2d),axis=0)
print("after joining 2d array axis = 0:\n",join_2d_array)

join_2d_array = np.concatenate((ar1_2d,ar2_2d),axis=1)
print("after joining 2d array axis = 1:\n",join_2d_array)

"""
Stacking is same as concatenation, the only difference is that 
stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which 
would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the 
stack() method along with the axis. If axis is not explicitly passed 
it is taken as 0.
"""

print("\nJoining Arrays Using Stack Functions:")
stack_join = np.stack((ar1,ar2),axis=0)
print("join 1d array using stack, axis=0:\n",stack_join)
stack_join = np.stack((ar1,ar2),axis=1)
print("join 1d array using stack, axis=1:\n",stack_join)

#hstack() to stack along rows. horizontal join
#vstack()  to stack along columns. vertical join
#dstack() to stack along height, which is the same as depth. diagonal join
print("\n")
print("array-1: ",ar1)
print("\narray 2: ", ar2)
print("\n")

print("join using hstack - according to row:\n" ,np.hstack((ar1, ar2)))
print("join using vstack - according to col:\n" ,np.vstack((ar1, ar2)))
print("join using dstack - according to diagonal:\n" ,np.dstack((ar1, ar2)))
print("\n")

print("..................array split..............\n")
"""
Splitting breaks one array into multiple.
We use array_split() for splitting arrays, 
we pass it the array we want to split and the number of splits.
"""

new_array = np.array([1,6,7,3,9,23,65,90,78])
print("1d array:",new_array)

x = np.split(new_array,3) # 3 = no.of splits
print("split 1d array:\n",x)

""" 
->If the array has less elements than required, it will adjust from the end accordingly.
->The return value of the array_split() method is an array containing each of the split as an array.
->If you split an array into 3 arrays, you can access them from the result just like any array element:
"""
print("array elements:")
print(x[0])
print(x[1])
print(x[2])
print("\n")

new_2d_array = np.array([[1,2],[3,4],[78,90],[90,67],[5,56],[78,45]])
print("2d array:\n",new_2d_array)

y = np.split(new_2d_array,3)
print("after spliting 2d array:\n",y)
print("array element")
print(y[0])
print("\n")
print(y[1])
print("\n")
print(y[2])
print("\n")

# you can specify which axis you want to do the split around.
z = np.split(new_2d_array,2,axis=1)
print("after spliting 2d array according axis 1:\n",z)
print("array element")
print(z[0])
print("\n")
print(z[1])
print("\n")
print(z[2])

"""
An alternate solution is using hsplit() opposite of hstack()
vstack() and dstack() are available as vsplit() and dsplit().

dsplit only works on arrays of 3 or more dimensions
"""