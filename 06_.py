f = open("data.txt","w")
f.write("Hello Python")
f.close()

f = open("data.txt","r")
print(f.read())
f.close()