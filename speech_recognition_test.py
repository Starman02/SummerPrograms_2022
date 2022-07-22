
import speech_recognition as sr

recognizer = sr.Recognizer()

macadamia_nuts = True

with sr.Microphone as source:
    while macadamia_nuts == True:
        audio = recognizer.listen(source)
        
        print(recognizer.recognize_sphinx(audio))