class Employee:
    language = "python"
    salary = 1200000
    company = "Google"

    def __init__(self , lang , name , sal): # constructor
        self.language = lang
        self.name = name
        self.salary = sal
        print("Employee is created") # dunder methord which is automatically call..

    def getinfo(self):

        print(f"The language is {self.language} . The salary is { self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("java script", "Harry" , 13000000)
print(harry.language, harry.name , harry.salary)
#harry.language = "java script"
#harry.greet()
#harry.getinfo() # Employee.getinfo(harry)

 #rohan = Employee()