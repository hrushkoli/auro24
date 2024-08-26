a = int(input("Max Range: "))

def primeCheck(var):
    if (var%2==0 or var%3==0 or var%5==0 or var%7==0):
        pass
    elif (var==0 or var==1):
        print(var," is not a prime nor composite")
    elif (var==2 or var==3 or var==5):
        print(var,"is a prime")
    else:
        print("%d is prime " % var)

for i in range(0,a+1):
    primeCheck(int(i))
