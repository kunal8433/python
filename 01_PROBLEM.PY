#display all tables from 0 to 6
for i in range (0,7):
    for j in range (1,10):
        print(f"{i} x {j} = {i*j}")
    print()

#display only [1] table
n= int(input("Enter the number:"))

for i in range (1,11):
    print(f"{n} x {i} = {n*i}")