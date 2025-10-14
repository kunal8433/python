class Employee:
    company = "Google"
    name = "kunal"
    def show(self):
        print(f"The name of the Employ is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC"
    name = "lucky"
    def showlang(self):
        print(f"The name of the Programmer is {self.name} and the language is {self.language}")

a = Employee()
b = Programmer()

print("WELLCOM TO MY WORLD")
print("ALL INFORMATION ARE THERE")
print()

print ("The company name is:",a.company ,
        "The name is :",a.name )
print()
print("The company name is:",b.company , 
      "The name is :",b.name )