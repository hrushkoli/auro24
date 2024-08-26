a = input("Enter a Number: ")
# print("len(a)=",len(a))
c=0

for i in range(0,len(a)):
    # print("i=",i)
    # print("a[i]",a[i])
    c+= pow(int(a[i]),len(a))
    # print("c=",c)

if (c==int(a)):
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")

