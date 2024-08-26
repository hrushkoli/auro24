a = input("Max Range = ")

def palindromeCheck(var):
    palCount=0
    for  i in range (len(var)-1,-1,-1):
        # print("i=",i)
        # print("var[i]=",var[i])
        # print("var[-i]=",var[-i-1])
        if(var[i]==var[-i-1]):
            palCount+=1
    if(len(var)==palCount):
        return True
    return False

print("the list of all palindrome numbers from 0,",a,"is :")

for i in range(0,int(a)+1):
    if(palindromeCheck(str(i))):
        print(i)
