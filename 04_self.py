class Employee:
    language = "python"
    salary = 1200000
    company = "Google"

    def getinfo(self):

        print(f"The language is {self.language} . The salary is { self.salary}")

    def greet(self):
        print("Good Morning sir")

    
    def respect (self):
        print("I respect to you")


harry = Employee()
harry.language = "java script"
harry.greet()
harry.respect()
harry.getinfo() # Employee.getinfo(harry)


