class programmer:
    company = "Microsoft"

    def __init__(self, salary , name , pincode):
     self.salary = salary
     self.name = name
     self.pincode = pincode 

kunal = programmer( 13000000 , "kunal" , 500081)
print(kunal.salary , kunal.name , kunal.pincode , kunal.company)