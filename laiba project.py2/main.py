import speech_recognition as sr
import webbrowser
import pyttsx3
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()
if __name__ == "__main__":
  speak("Initialing jarvis....")
  #listen for the wake word"jarvis
  #obtain audio from the microphone
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening...")
    audio = r.listen(source)
    
  # recognize speech using Sphinx
  try:
    command = r.recognize_google(audio)
    print(command)
  except sr.UnknownValueError:
    print("Sphinx could not understand audio")
  except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))  



