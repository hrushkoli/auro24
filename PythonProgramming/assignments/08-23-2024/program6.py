# String Library example

str = "Hello"
str2 = "Friend"

print(str) # To print the entire string

print(str[1]) # To print the character at index 1

print(str[:1]) # To print all characters till index 1

print(str[-1]) # To print the second last index

print(str[0:2]) # To Slice the String

print(str[::3]) # To Slice 2the String

print((str+str2)*2) # To Append and perform operations on string`

print("w" in str2) # Searches for 'w' in str2

print("e" in str2) # Searches for 'e' in str2

print("my string is %s"%(str+str2)) # Adding variables to string

print("{} and {} are my friends".format("mahesh","manav")) # example of curly bracket formatting

print("{0} and {1} are my friends".format("mahesh","manav")) # example of curly bracket formatting with positional arguments


print("{u},{b} and {c} are the languages of IT".format(u="java",b="ml",c="python")) # example of curly bracket formatting with arguments

del str # To delete the string from memory
