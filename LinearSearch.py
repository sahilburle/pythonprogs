#pos = -1

def linearSearch(list, n):
    #i = 0

    # while i < len(list):
    #     if list[i] == n:
    #         globals() ['pos'] = i
    #         return True;
    #     i = i + 1
    #
    # return False

    for i in range(0, len(list)):
        if (list[i] == n):
            return i
    return -1

list = [5,8,4,6,9,2]

n = 4

result = linearSearch(list,n)

if result == -1:
    print('not found')
else:
    print('found')


'''
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1  
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45  
  
# Function call   
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")
'''