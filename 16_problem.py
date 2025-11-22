a = int(input("Enter your number 1:"))
b = int(input("Enter your number 2:"))
c = int(input("Enter your number 3:"))
d = int(input("Enter your number 4:"))
if a>b and a>c and a>d:
    print("The greatest number is:",a)
elif b>a and b>c and b>d :
    print("The gratest number is :",b)
elif c>a and c>b and c>d :
    print("The greatest number is :",c)
else:
    print("The greatest number is :",d)