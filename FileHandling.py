f = open('MyData','r')

f1 = open('abc','w')
#f1.write("Something")
#print(f.read())             #for reading

for data in f:
    f1.write(data)


"""
is it a COMMENT..
kind of documentation
"""