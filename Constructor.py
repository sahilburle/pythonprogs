class Computer:

    def __init__(self):
        self.name = 'navin'
        self.age = 28

        # def update(self):
        #     self.age = 30

        def compare(self, other):
            if self.age == other.age:
                return True
            else:
                return False

c1 = Computer()
c2 = Computer()

# c1.name = 'rashi'
# c1.age = 12

if c1.compare(c2):
    print("they r same")

# c1.update()

print(c1.name)
print(c2.name)