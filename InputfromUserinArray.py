from array import *

arr = array('i',[])

n = int(input("Enter the length of array\t"))

for i in range(n):
    x = int(input("Enter the next value\t"))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search\t"))

k = 0
for e in arr:
    if e==val:
        print(k)
        break

    k+=1

print(arr.index(val))