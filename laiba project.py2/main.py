import speech_recognition as sr
import webbrowser
import pyttsx3
import naatlibrary
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def process_command(c): 
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open tiktok" in c.lower():
    webbrowser.open("https://tiktok.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  elif c.lower().startswith("play"):
    naat = c.lower().split(" ")[1]
    link=naatlibrary=naat[song]
    webbrowser.open(link)

  
if __name__ == "__main__":
  speak("Initialing jarvis....")
    #listen for the wake word"jarvis
    #obtain audio from the microphone
  r=sr.Recognizer()

  while True:
    print("recognizing...")
    try:
      with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
      word = r.recognize_google(audio)
      if (word.lower() == "jarvis"):
        speak("yes")
      #listen for command
        with sr.Microphone() as source:
          print("jarvis active...")
          audio = r.listen(source , timeout=2, phrase_time_limit=1)
          command = r.recognize_google(audio)

          process_command(command)
    except Exception as e:
      print(" error; {0}".format(e))  



