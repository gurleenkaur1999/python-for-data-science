import numpy as np
a = np.arange(start=1, stop=10, step=1)
#here we ctrl what should be the increment
print(a)
#creates an array with evenly spaced numbers
#here we ctrl amount of vaues we need
b=np.linspace(start=1,stop=3,num=3)
print(b)
c=np.linspace(start=1,stop=3,num=10)
print(c)
#zeros
#Creates an array full of 0s.
np.zeros(5)
#Reshape a 1D array of 24 elements into different shapes 
a.reshape(3,3)
#start = default 0 → start at the first element
#end = default → go till the last element
#step = 3 → take every 3rd element
a[0::4]
#reverse an array
a[::-1]
# get specific rows/columns from 2D arrays
x=np.array([[1,2,3],
           [4,5,6]])
#0th column
x[:,0]
#2nd column
x[:,2]
#1st row
x[1]
#Perform element-wise operations: add 10 to all elements, multiply arrays, apply mathematical functions
x+10
x*10
x-2