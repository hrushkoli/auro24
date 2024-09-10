class Student:
    def __init__(self,x,y): 
        self.a = 10
        self.name = x
        self.city = y

    def m1(self):
        print(self.name)
        print(self.city)

s = Student("Oswald","Surat")
s.m1()
