def binarySearch(list, no, low, high):

    if high >= low:

        mid = (high + low)//2

        #at mid
        if list[mid] == no:
            return mid

        #for left half
        elif list[mid] > no:
            return binarySearch(list, no, low, mid-1)

        #for right half
        else:
            return binarySearch(list, no, mid+1, high)

    else:
        return -1

list = [2,3,4,6,7,8,9,11]

no = 11

result = binarySearch(list, no, 0, len(list)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print('not found')