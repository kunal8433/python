class Employee:
    a = 1


    @classmethod
    def show(self):
        print(f"The value of a is {self.a}")

    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self, value):
        self.ename = value
    

e = Employee()
e.a = 45
e.name = "Kunal malik"
print(e.name)
e.show()

