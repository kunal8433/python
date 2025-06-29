
def MULTIPLY_two_digits(a, b):
    return a - b
# Input from the user
try:
    num1 = int(input("Enter the first digit 1: "))
    num2 = int(input("Enter the second digit 2: "))
    # Calculate the NUMBER
    result = MULTIPLY_two_digits (num1, num2)
    # Display the result
    print(f"The multiply of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid integers.")