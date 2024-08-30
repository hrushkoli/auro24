# Python has a concept of multiple chaining

a = int(input("enter percentage : "))

if (a<0):
    print('Invalid input')
if (a<35):
    print('Fail')
if (a>=35 and a<45):
    print('Pass')
if (a>=45 and a<55):
    print('Average')
if (a>=55 and a<60):
    print('Good')
if (a>=60 and a<70):
    print('Very Good')
if (a>=70 and a<=100):
    print('Distinction')

