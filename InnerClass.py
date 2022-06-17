class Student:

    def __init__(self,  name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name , self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

s1 = Student('navin', 2)
s2 = Student('jenny', 3)

s1.show()