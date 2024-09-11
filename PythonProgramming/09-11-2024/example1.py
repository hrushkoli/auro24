class Emp:
    def __init__(self,eno,ename,salary):
        self.eno = eno
        self.ename = ename
        self.salary = salary
    
    def empInfo(self):
        print("Employee Number is ",self.eno)
        print("Employee Name is ",self.ename)
        print("Employee Salary is ",self.salary)

list_emp = []

while True:
    eno = input("Enter Employee Number: ")
    ename = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    e = Emp(eno,ename,salary)
    list_emp.append(e)
    print("Employee Record Inserted Successfully")

    choice = input("Do you want to add more records? Type Yes or No: ")
    if(choice.lower()=='no'):
        break

for emp in list_emp:
    emp.empInfo()
