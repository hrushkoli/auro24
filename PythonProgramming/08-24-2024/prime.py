a = int(input("Enter a Number: "))

if (a%2==0 or a%3==0 or a%5==0 or a%7==0 ):
    print("%d is not a prime" % a)
elif (a==0 or a==1):
    print(a," is not a prime nor composite")
elif (a==2 or a==3 or a==5):
    print(a,"is a prime")
else:
    print("%d is prime " % a)

