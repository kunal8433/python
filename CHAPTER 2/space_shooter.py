
# Tiny No-Import Guessing Game
print("Guess the Number (1-10)")
secret = 7
tries = 3

while tries > 0:
    guess = int(input("Your guess: "))
    if guess == secret:
        print("You won!")
        break
    print("Higher tera ba!" if guess < secret else "Lower!")
    tries -= 1

if tries == 0:
    print(f"Game Over! Number was {secret}")