class Student:
    def __init__(self): 
        self.a = 10
        print(id(self))

    def attendance():
        print("From attendanse");

s = Student()
s.a = 15
print(s.a)
print(id(s))

s1 = s 
print(s1.a)
print(id(s))


