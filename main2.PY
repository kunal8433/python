import random

# 🎮 Game Title
print("🎮 Welcome to  KUNAL MALIK Rock Paper Scissors Game!\n")

# 📊 Score System
user_score = 0
computer_score = 0

# 🔁 Game Loop
while True:
    print("\nChoose your move:")
    print("r 👉 Rock 🪨")
    print("p 👉 Paper 📄")
    print("s 👉 Scissor ✂️")

    yourstr = input("Enter your choice (r/p/s) or q to quit: ").lower()

    # ❌ Exit Option
    if yourstr == "q":
        print("\n👋 Exiting Game...")
        break

    # ⚠️ Input Validation
    yourdict = {"r":1, "p":2, "s":3}
    if yourstr not in yourdict:
        print("❌ Invalid input! Try again.")
        continue

    # 🤖 Computer Choice
    computer = random.choice([1,2,3])
    maindict = {1:"Rock 🪨", 2:"Paper 📄", 3:"Scissor ✂️"}

    you = yourdict[yourstr]

    # 📢 Show Choices
    print(f"\n🤖 Computer chose: {maindict[computer]}")
    print(f"👤 You chose: {maindict[you]}")

    # 🏆 Game Logic
    if computer == you:
        print("🤝 It's a Draw!")
    elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💻 Computer Wins!")
        computer_score += 1

    # 📊 Show Score
    print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

# 🏁 Final Result
print("\n🏁 Final Score:")
print(f"👤 You: {user_score} | 🤖 Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You are the Champion!")
elif user_score < computer_score:
    print("😢 Computer is the Champion!")
else:
    print("🤝 It's a Tie Overall!")