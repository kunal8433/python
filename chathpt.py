import random
'''
1 for snake 
0 for gun 
-1 for water
'''
computer = random.choice([1,0,-1])
print("Welcom to my first game {gun,water,snake}")
print("1:snake , 0:gun , -1:water")
youstr = (input("Enter your choice :"))
yourDict = {"s":1,"w":-1,"g":0}
computerDict = {1:"snake",0:"gun",-1:"water"}

you = yourDict[youstr]

print(f"you chose {computerDict[you]}\n computer chose{computerDict[computer]}")
if(computer == you):
    print("match draw")

else:
    if(computer == -1 and you == 1):
        print("YOU WIN!")

    elif(computer == -1 and you == 0):
        print("YOU LOSS!")

    elif(computer == 1 and you == -1):
        print("YOU LOSS")

    elif(computer == 1 and you == 0):
        print("YOU WIN!")

    elif(computer == 0 and you == -1):
        print("YOU WIN!")

    elif(computer == 0 and you == 1):
        print("YOU LOSS!")
    
    else:
        print("something went wrong")