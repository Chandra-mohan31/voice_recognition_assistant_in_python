import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from time import ctime
import webbrowser
import random
import tkinter as tk
from tkinter import filedialog
#import time

def speak(reply):
    tts=gTTS(text=reply,lang="en")
    r=random.randint(1,10000000)
    filename='audio-'+str(r)+".mp3"
    tts.save(filename)
    playsound.playsound(filename)




def get_audio(ask=False):
    mic = sr.Microphone()
    r=sr.Recognizer()
    with mic as source:
        if ask:
            print(ask)
            speak(ask)
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        said=""
        try:
            said = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry i did not get it")
            speak("sorry i did not get it")    
        except sr.RequestError:
            print("sorry,unable to recgonize") 
            speak("sorry,unable to recognize")   
    return said




def respond(text):
    if "hello" in text:
        speak("hello, how are you") 
    if "name" in text:
        speak("my name is love")
    if "time" in text:
        print(ctime) 
    if "search" in text:
        search = get_audio("what do you want to search for?")         
        url="https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak("here is what i found for you")
    if "location" in text:
        location=get_audio("what is the location?")
        url="https://google.nl/maps/place/"+location + "/&amp;"
        webbrowser.get().open(url)
        speak("here is the location of"+location)
    if "application" in text:
        speak("choose the exe file of the app to open")
        filename=filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("executables","*exe"),("all files","*.*")))
        os.startfile(filename)
    

speak("how can i help you")
print("how can i help you ?")
#text=input()
text=get_audio()
respond(text)
