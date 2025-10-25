a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ValueError("Denominator cannot be zero.")
else:
    print(f"Result: {a / b} ")