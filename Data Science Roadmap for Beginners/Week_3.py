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
a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim) # .ndim method returns the dimension of the array 
print(a.dtype) # .dtype method returns the datatype of the elements 
a1 = np.array([[1,2],[3,4],[5,6]], dtype=float)
a2 = np.array([[1,2],[3,4],[5,6]], dtype=float)
print(a2.itemsize)
print(a1.itemsize)
print(a2.size) # .size method returns the amount of elements of the numpy array 
print(a2.shape) # .shape method returns the size of the array, rows and columns 

np.zeros((3,4)) # .zeros method creates an array with zero values and 3,4 shape
np.ones((3,4)) # similar but with ones
np.arange(1,5) # will create an array from 1 to 4, so 1,2,3,4
np.arange(1,5,2) # stisl will create an array from 1 to 4 with a step of 2, so it will be 1,3
np.linspace(1,5,10) # this will create an array from 1 to 4 with 10 elements in total, linearly spaced
a.reshape(2,3) # .reshape method will reshape the array to 2 rows and 3 columns 

print(a1.sum(axis=0)) # axis 0 is the columns 
print(a1.sum(axis=1)) # axis 1 is the rows

# Slicing and indexing - same as python lists 
a = np.array([[6,7,8], [1,2,3], [9,3,2]])
for row in a:
        print(row)

for cell in a.flat: # .flat method flattens the array and returns a single dimension array 
        print(cell)
        
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)

for row in a,b:
        print(row)

print(np.vstack((a,b))) # stacks the two arrays vertically
print(np.hstack((a,b))) # stacks the two arrays horizontally

a = np.arange(12).reshape(3,4)
for cell in a.flatten(): # .flat and .flatten() the same method 
        print(cell)