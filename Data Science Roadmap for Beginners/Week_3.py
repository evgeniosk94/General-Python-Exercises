import numpy as np
import sys
import time

# Benefits of using numpy arrays
# Less memory, fast and convinient 

a = np.array([1,2,3]) # Create a numpy array, pass on your list. Same or very simialr to a list
print(a)

# Check the memory of numpy array and normal python list
list = range(1000) # make a python list of 1000 elements 
print("size of python list is:", sys.getsizeof(1)*len(list)) # this gets the size of one element of the list times the number of elements = total size of the list

array = np.arange(1000) # arange is the same to range. arange is the format for numpy 
print("size of numpy arrays is:", array.size*array.itemsize) # .size method gives the amount of elements of the array (like len), .itemsize method gives the size of a single element 

# Check fast and convinient 
size = 1000000

list1 = range(size) 
list2 = range(size)

array1 = np.arange(size)
array2 = np.arange(size)
# python list
start = time.time()
result = [(x+y) for x,y in zip(list1,list2)] # zip here will add the element 1 of list1 to element 1 of list2 and so on, list comprehension 
print(f"python list took: ", round((time.time()-start)*1000,3),"msec to execute") # 1000 to have better time scale for comprarisson 
# numpy array 
start = time.time()
result = array1 + array2 # easier to comprehend numpy arrays than python lists 
print(f"numpy array took: ", round((time.time()-start)*1000,3), "msec to execute")

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)

# Basic array operations 
