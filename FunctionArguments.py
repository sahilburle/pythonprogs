
def update(x):

    print(id(list))

    list[1] = 25
    print(id(list))
    print("x ",x)

list = [10,20,30]
print(id(list))

update(list)
print("a ",list)