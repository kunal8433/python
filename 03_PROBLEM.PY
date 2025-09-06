p1= "Make a lot of money"
p2= "buy now"
p3="click this"
p4="subscribe this"
message=input("Enter your coment :")

if((p1 in message) or (p2 in message) or (p3 in message)or(p4 in message)):
    print("This is a spam message")
else:
    print("This is a not spam message")