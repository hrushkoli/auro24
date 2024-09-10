class Student:
    x = 'abc'
    y = 'xyz'

    def m1(self):
        print(self.x)
        print(self.y)
        print(id(self))

    def m2(self,student):
        print(id(self))
        student.m1()

s = Student()
s.m1()
s.m2(s)
print(id(s))
