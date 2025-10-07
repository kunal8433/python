import random

'''
1 for snake
0 for gun
-1 for water
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, g for gun, w for water): ")

youdict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("Match draw")
elif (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
    print("YOU WIN!")
else:
    print("YOU LOSS!")
