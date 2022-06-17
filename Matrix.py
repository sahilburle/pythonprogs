from numpy import *

arr1 = array([
                [1,2,3,7,8,9],
                [4,5,6,9,8,7]
             ])

arr2 = arr1.flatten()       #to convert 2d array to 1d

arr3 = arr2.reshape(2,2,3)

print(arr3)

m = matrix('1 2 3 4 ; 5 6 7 8')

print(m)