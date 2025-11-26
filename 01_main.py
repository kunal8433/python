import speech_recognition as sr
import webbrowser

import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speek(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "main__":
    speek("Hello, how can I assist you today?")

