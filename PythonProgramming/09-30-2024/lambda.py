a = int(input("Enter value of A"))
b = int(input("Enter value of B"))


while True:
    print("What operations would you like to perform? \n 1 for A+B:  \n 2 for A-B:  \n 3 for A*B:  \n 4 for A/B: \n 0 to Exit:  \n")
    operation = int(input())

    if(operation==0):
        break

    if(operation==1):
        print("Output of Addition is: ",(lambda a,b : a+b)(a,b))

    if(operation==2):
        print("Output of Subtraction is: ",(lambda a,b : a-b)(a,b))

    if(operation==3):
        print("Output of Multiplication is: ",(lambda a,b : a*b)(a,b))

    if(operation==4):
        print("Output of Division is: ",(lambda a,b : a/b)(a,b))
