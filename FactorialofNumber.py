
# def fact(n):
#
#     f = 1
#
#     for i in range(1,n+1):
#         f = f*i
#
#     return f
#
# x = 5
#
# result = fact(x)
#
# print(result)


#             ------------- Recursion ------------------

def fact(n):

    if (n==0):
        return 1

    return n * fact(n-1)


result = fact(5)

print(result)