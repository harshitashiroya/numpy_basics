import numpy as np

"""
The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, 
and any changes made to the original array will affect the view.


"""
print("copy and view")
print("copy")
cp = np.array([23, 65, 1345])
print(cp)
new_cp = cp.copy()
print(new_cp)
new_cp[1] = 600
print("after changing new_cp:", new_cp)
print("no changes in cp after changing new_cp:", cp)
print("\nview")
vi = np.array([23, 8, 2])
print(vi)
new_vi = vi.view()
print(new_vi)
new_vi[2] = 100
print(new_vi)
print(vi)
print("\n")