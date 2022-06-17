
def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even, odd

lst = [9,8,7,6,5,4,3,2,1]

even, odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))
#print(odd)