from functools import reduce

# def is_even(n):
#     return n%2==0

# def update(n):
#     return n+2

#

nums = [3,5,4,8,2,9,4,8]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2, evens))

#sum = reduce(add_all, doubles)

sum = reduce(lambda a,b : a+b, doubles)

print(sum)

print(evens)

print(doubles)