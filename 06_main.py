import random
'''
g for gun
w for water 
s for snake
'''

computerstr = random.choice([1,-1,0])
print("WELCOME TO KUNAL GUN,WATER,SNAKE GAME")
print("s for snake \nw for water \ng for gun")
yourstr = input("Enter your choice")
yourDict ={"s":1 ,"w":0 ,"g":-1}
computerDict = {1:"snake" , -1:"gun", 0:"water"}

you = yourDict[yourstr]
print(f"You chose {yourDict[yourstr]}\nComputer chose {computerDict[computerstr]}")  # IMPORTANT

if you==computerstr:
    print("MATCH DRAW")

else:
    if (computerstr== -1 and you==1):
        print("YOU WIN")
    elif (computerstr== -1 and you==0):
        print("YOU WIN")
    elif (computerstr== 1 and you==-1):
        print("YOU LOSS")
    elif (computerstr== 1 and you==0):
        print("YOU LOSS")
    elif (computerstr== 0 and you==1):
        print("YOU WIN")
    elif (computerstr== 0 and you==-1):
        print("YOU LOSS")
    else:
        print("Something went wrong")



