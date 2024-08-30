# Swapping Values of a , b , c & d
a = 15
b = 10
c = 13
d = 20

print("Before Swapping: ")
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)

a,b = d,c

print("After Swapping: ")
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)

# This works even if you try to swap values of different data types since variables are stored as objects 

x = 10
y = 'abc'

print("Before Swapping: ")
print('x=',x)
print('y=',y)

x,y = y,x

print("After Swapping: ")
print('x=',x)
print('y=',y)

