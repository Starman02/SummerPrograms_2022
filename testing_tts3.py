from locale import atoi
import pyttsx3
 
a1 = "say what again, say what one more god damn time, i dare ya, I double dare ya motherfucka"

# speaking_engine()



class ADAM_SPEECH_V1:
    def __init__(self, sentence='welcome to adam'):
        self.__sentence = sentence

	
    def set_sentence(self, sentence):
        self.sentence = sentence


    def get_sentence(self):
        return self.sentence       


    def speaking_engine(self, sentence):
        # init function to get an engine instance for the speech synthesis
        engine = pyttsx3.init()
        
        # say method on the engine that passing input text to be spoken
        engine.say(sentence)
        
        # run and wait method, it processes the voice commands.
        engine.runAndWait()











# abble = ADAM_SPEECH_V1()

# print("waiting 3 seconds")
# import time
# time.sleep(3)
# abble.speaking_engine(a1)


