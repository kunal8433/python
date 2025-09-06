mark1 = int(input("Enter Marks 1:"))
mark2 = int(input("Enter Marks 2:"))
mark3 = int(input("Enter Marks 3:"))

#Check for total percentage
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100
if(total>=40 and mark1 >=33 and mark2 >=33 and mark3 >=33):
    print("Student is passed with percentage:", percentage)
else:
    print("Student is failed with percentage:", percentage)