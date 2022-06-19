a = 5
b = 0

try:
    print(a/b)

except ZeroDivisionError as e:
    print('not divide by zero')

finally:
    print('resource closed')

