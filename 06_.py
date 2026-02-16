import random
choice = input("Enter your choice (y/n)")
computer = random.choice[(1,2),(3,4),(5,6),
            (1,3),(2,4),(5,1),
      
          (6,2),(3,5),(4,6)]
while True :

       if choice == "y":

         print("You rolled a", computer)
       elif choice == "n":
         print("You chose not to roll the die.")
       else:
         print("Invalid input. Please enter 'y' or 'n'.")