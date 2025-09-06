a = int(input("Enter your age: "))
if (a >= 18):
    print("You are above the age of consent")
    print("Good well done")
elif(a<0):
    print("Your are entring an invalid age")
elif(a==0):
    print("You are entring a0 which is not an valid age")
else:
    print("You  are below the age of consent")
print("End the program")
