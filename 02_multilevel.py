class Emploee:
    a = 1

class Manager(Emploee):
    b = 2

class Programmer(Manager):
    c = 3

o = Emploee()
print(o.a)
#print(o.b) # AttributeError: 'Emploee' object has no attribute 'b'

o = Manager()
print(o.a)

