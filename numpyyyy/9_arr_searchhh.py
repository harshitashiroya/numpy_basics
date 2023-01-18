import numpy as np

#To search an array, use the where() method.

search_arr = np.array([2,6,7,9,9,23,45,78,9,90])
print(search_arr)

x = np.where(search_arr == 9) # will return a tuple which contain index number
print("search_arr == 9")
print(x)
print("\n")

y= np.where(search_arr%3 == 0)
print("%3 == 0")
print(y)
print("\n")

#Find the indexes where the values are odd
print("values are odd")
z = np.where(search_arr%2 == 1)
print(z)

"""
Search Sorted

There is a method called searchsorted() which performs a binary search in the array, 
and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.
"""
print("\n")
print("search shorted")
sort_array = np.array([1,3,5,6,8,90,100])
print("sorted array is:",sort_array)

#Find the indexes where the value 7 should be inserted:
x = np.searchsorted(sort_array,7)
print("7 inserted at index:",x)

"""
Search From the Right Side
By default the left most index is returned, 
but we can give side='right' to return the right most index instead.
"""

#Find the indexes where the value 120 should be inserted, starting from the right:

y = np.searchsorted(sort_array,120,side="right")
print(y)


#multiple value
x = np.searchsorted(sort_array, [2, 4, 6])
print("for multiple value",x)