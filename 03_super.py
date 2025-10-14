class Employee:
    def  __init__(self):
        print("Counstructor of Employee")

    a = 1

class programmer(Employee):
    def  __init__(self):
        print("Counstructor of Programmer")
        
    b = 2

class Manager(programmer):
    def  __init__(self):
        print("Counstructor of manager")
        
    c = 3

o = Manager()
print(o.a,o.b,o.c)
