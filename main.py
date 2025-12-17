import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
         speak("Opening Google")
         webbrowser.open("https://www.google.com")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "AskMe"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                 speak("How can I help you?")
                 # Listen for command
                 with sr.Microphone() as source:
                    print("Jarvis Active...")
                    command = r.recognize_google(audio)
                    processCommand(command)
        
        except sr.UnknownValueError:
             print("Could not understand audio")