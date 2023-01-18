import numpy as np


"""
Slicing arrays

Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""
print("slicing in 1D array")
sli_1D = np.array([23, 34, 57, 35, 576, 545, 254, 6])
print("array is: ", sli_1D)
print("1:4 ->", sli_1D[1:4])  # 1 index include 4th index exclude
print("2 to end: ", sli_1D[2:])
print("start to 5th index: ", sli_1D[:6])
print("all element:", sli_1D[:])
print("negative slicing -5 to -2:", sli_1D[-5:-2])  # -5 include, -2 exclude
print("using step: ", sli_1D[1:7:2])  # skip one element
print("\n")

print("slicing in 2D array")
sli_2D = np.array([[1, 2, 4, 2132, 435], [3, 4, 56, 50, 52]])
print("2D array is:\n", sli_2D)
print(sli_2D[1, 1:3])  # 1st = index 2nd = slicing range
print("From both elements, return index 2:", sli_2D[0:2, 2])
print("From both elements, slice index 1 to index 4 (not included), "
      "this will return a 2-D array:\n", sli_2D[0:2, 1:4])
print("\n")
