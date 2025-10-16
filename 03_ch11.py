class Emploee:
    company = "Google"
    name = "Kunal Malik"

class Programmer(Emploee):
    company = "Microsoft"
    name = "Ankit Malik"

a = Emploee()
b = Programmer()

print(a.company)
print(a.name)
print(b.company)
print(b.name)