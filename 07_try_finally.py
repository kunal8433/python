try:
    a = int(input("Hey, enter a number: "))
    print(a)

except Exception as e:
    print(e)


finally:
    print("I am inside finally block")
    