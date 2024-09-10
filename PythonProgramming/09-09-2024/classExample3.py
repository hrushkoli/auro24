class Student:
    x = 'abc'
    y = 'xyz'

    def m1(self):
        print(id(self))

s = Student()
s.m1()
print(id(s))
