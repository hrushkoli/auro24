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

# if (a<0):
#     print('Invalid input')
# if (a in range(0,35)):
#     print('Fail')
# if (a in range(35,45)):
#     print('Pass')
# if (a in range(45,55)):
#     print('Average')
# if (a in range(55,60)):
#     print('Good')
# if (a in range(60,70)):
#     print('Very Good')
# if (a in range(70,101)):
#     print('Distinction')
