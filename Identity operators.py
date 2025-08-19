#Python program to illustrate the use
# of 'is' identfty operator
x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x=5.0
if (type(x) is float):
    print("true")
else:
    print("false")

x = 20
y = 20
if ( x is y):
    print("x & y SAME identity")
y=30
if ( x is not y):
    print("x and y have DIFFERENT identity")

a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a in c)
print(a not in b)
print (a in c)
print(a not in b)