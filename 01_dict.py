Marks ={
    "Kunal": 100,
    "Lucky":43,
    "Ankit":23}
print(Marks,type(Marks))

print(Marks["Kunal"])   
# print(Marks["Rohit"])   #KeyError: 'Rohit'
print(Marks.get("Rohit"))  #None
print(Marks.get("Rohit","Not Found"))  #Not Found
print(Marks.get("Kunal","Not Found"))  #100
Marks["Kunal"]= 99
print(Marks)
    

