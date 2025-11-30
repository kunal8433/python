import random
'''
1 for snake 
2 for water 
3 for gun 

'''

computer = random.choice([1,2,3])
maindict = {1:"snake" , 2:"water" , 3:"gun"}
youdict = {"s":1, "g":2 , "w":3}
print("WELCOM TO MY GAME")
print()
print("1 for snake")
print("2 for water")
print("3 for gun")

yourstr = input("Enter your choice:")

you = youdict [ yourstr]



print(f"You  chose {maindict[you]}/n computer chose {maindict[computer]}")

if computer == you :
    print("MATCH DRAW!")

else :
    if computer == 1 and you == 1 :
        print("YOU WIN !")
    elif computer == 1 and you == 2 :
        print("YOU loss !")
    elif computer == 1 and you == 3 :
        print("YOU loss !")
    elif computer == 3 and you == 2 :
        print("YOU loss !")
    elif computer == 2 and you == 3 :
        print("YOU loss !")
    elif computer == 1 and you == 1 :
        print("YOU loss !")
    elif computer == 3 and you == 2 :
        print("YOU loss !")
    elif computer == 2 and you == 1 :
        print("YOU loss !")
    else:
        print("error")

