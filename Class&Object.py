class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("i5, 16gb, 1tb")

com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

com1.config()
com2.config()

print(type(com1))
