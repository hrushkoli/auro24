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
        print(student.x)
        print(self.x)

s = Student()
print(s.x)
s.m1()
s.x = 30
s.m2(Student())
print(id(s))
