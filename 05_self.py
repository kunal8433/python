class Employee:
    language = "python"
    salary = 1200000
    company = "Google"

    def getinfo(self):

        print(f"The language is {self.language} . The salary is { self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
harry.language = "java script"
harry.greet()
harry.getinfo() # Employee.getinfo(harry)


