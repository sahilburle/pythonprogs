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