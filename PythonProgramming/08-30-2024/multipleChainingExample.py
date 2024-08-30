# Python has a concept of multiple chaining

a = int(input("enter percentage : "))

if (a<0):
    print('Invalid input')
if (0<=a<=35):
    print('Fail')
if (35<=a<=45):
    print('Pass')
if (45<=a<55):
    print('Average')
if (55<=a<60):
    print('Good')
if (60<=a<70):
    print('Very Good')
if (70<=a<=100):
    print('Distinction')

