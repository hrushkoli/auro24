# Example of Type Conversion

# There are 4 types of Data 
#  -- Binary
#  -- Decimal
#  -- Octal
#  -- Hexa

x = 123
y = bin(x)
print(y)
print(0b1111011) ## Print converts the binary value to decimal and prints it

a = 0o657
print(type(a))
print(type(0o657))
print(a) ## Print converts the octal number to decimal and prints it

b = 0x657abc
print(b) ## Print converts the hexa number to decimal and prints it

c = oct(x)
print(c)

d = 0b101110110
z = oct(d)
print(z)
