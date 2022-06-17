
num = 12

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print("Not prime")
else:
    print("Prime")