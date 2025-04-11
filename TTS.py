import pyttsx3

engine = pyttsx3.init()

while True:
    input1 = input("Type Something : ")
    engine.setProperty('rate', 150)
    engine.say(input1)
    engine.runAndWait()