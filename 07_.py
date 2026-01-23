while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exited")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        print("Result:", a / b)
    else:
        print("Invalid choice")
