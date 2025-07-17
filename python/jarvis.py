import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("hello i am jarvis! how may i help you sir")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=200
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-us")
        print(f"user said :\n{query}")
    except Exception as e:
        print("please say again could not recognize")
        return "none"
    return query
        


if __name__ =="__main__":
    # speak("this is my first time doing this")
    wishme()
    while True:
        query=take_command().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query , sentences=4)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the current time is {strTime}")
        elif 'open zoom' in query:
            zoom="C:\\Users\\Ankita Gupta\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoom)
        elif 'bye' in query:
            speak("goodbye")
            exit()
            

