m1 = int(input("Enter your Marks 1:"))
m2 = int(input("Enter your Marks 2:"))
m3 = int(input("Enter your Marks 3:"))
#total marks == 40%
# required marks to pass == 33%
total = m1 + m2 + m3
percentage = (total / 300) * 100
if m1<33 or m2<33 or m3<33:
    print("The student Fail winth persentage:",percentage)

else:
    print("The student pass winth :", percentage)