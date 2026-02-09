def is_prime(n):
    for i in range(1,50):
        if n % i == 0:
            print(i)
        else:
            print("Not a prime number")
number = int(input("Enter a number: "))
is_prime(number)
    