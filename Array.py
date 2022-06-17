from array import *

vals = array('i',[5,9,8,4,2])

new_val = array(vals.typecode, (a*a for a in vals))   #for loop will assign 1 - 1 value to

vals.reverse()

# for e in new_val:
#     print(e)

i = 0

while(i<len(new_val)):
    print(new_val[i])
    i+=1