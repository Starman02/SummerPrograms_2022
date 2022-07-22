import pyttsx3
 
a1 = "say what again, say what one more god damn time, i dare ya, I double dare ya motherfucka"

def speaking_engine():
    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    
    # say method on the engine that passing input text to be spoken
    engine.say(a1)
    
    # run and wait method, it processes the voice commands.
    engine.runAndWait()

speaking_engine()



