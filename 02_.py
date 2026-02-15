import random
n = random.choice([1,100])
a = -1
guess = 0 
while(a!=n):
    a = int(input("Enter your number:"))
    if (a>n):
        print("guess lower number")
    elif (a<n):
        print("higher number plss")
    
        guess+1
print(f"you have guess the number {n} correctliy in {guess} attempt")    

