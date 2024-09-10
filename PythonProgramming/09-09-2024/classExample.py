class Student:
    def __init__(self): 
        self.a = 10
        print(id(self))

    def attendance():
        print("From attendanse");

s = Student()
print(s.a)
print(id(s))

s1 = s 
print(id(s))
