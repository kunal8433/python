import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to Kunal Robo Speaker 1.1")
    print()

    while True:
        x = input("Enter your command (type 'exit' to quit): ")
        if x == "e":
            engine.say("Exiting the program. Goodbye!")
            engine.runAndWait() 
            
            break

        engine.say(x)
        engine.runAndWait()
