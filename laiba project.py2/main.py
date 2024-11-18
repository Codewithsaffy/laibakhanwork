import speech_recognition as sr
import webbrowser
import pyttsx3
import aifc

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()
if __name__ == "__main__":
  speak("hey sir i am fine what can i do for you")
  
# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello, I am your assistant.")
# engine.runAndWait()

