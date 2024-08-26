a = input("enter any number = ")
# print("len(a)=",len(a))
palCount=0

for  i in range (len(a)-1,-1,-1):
    # print("i=",i)
    # print("a[i]=",a[i])
    # print("a[-i]=",a[-i-1])
    if(a[i]==a[-i-1]):
        palCount+=1

if(len(a)==palCount):
    print("Palindrome")
else:
    print("Not a Palindrome")
