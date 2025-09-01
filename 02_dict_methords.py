Marks ={
    "Kunal": 100,
    "Lucky":43,
    "Ankit":23,
    0:"Kunal"

}

print(Marks.items()) 
print(Marks.keys())
print(Marks.update())

Marks.update({"lucky":56,"jaat":78})
print (Marks)
print (Marks.get("Kunal")) #print the value of Kunal
print(Marks.get("Kunal1")) #print none if not found
print(Marks["Kunal"]) #print the value of Kunal
#print(Marks["Kunal1"]) #print error if not found

print(Marks.pop("Kunal")) #remove the key value pair
print(Marks)
print(Marks.popitem()) #remove the last key value pair
print(Marks)







