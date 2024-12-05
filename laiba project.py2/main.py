import speech_recognition as sr
import webbrowser
import pyttsx3
import naatlibrary
import requests
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="60180e78c4d0469c926ae6aa1b95abc6"

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
    song=c.lower().split(" ")[1]
    link=naatlibrary.naat[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    if r.status_code == 200:
    # Parse the JSON response
      data = r.json()
    # Extract and print the headlines
      articles = data.get("articles", [])
        # print"Top Headlines:"
      for article in articles:
        speak(article['title'])

  
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
      if (word.lower() == "alexa"):
        speak("yes")
      #listen for command
        with sr.Microphone() as source:
          print("jarvis active...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          process_command(command)
    except Exception as e:
      print(" error; {0}".format(e))  



