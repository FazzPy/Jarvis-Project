import speech_recognition as sr
import pyttsx3
from pygame import mixer
import time
from colorama import Fore, Back, Style
import colorama

colorama.init(autoreset=True)

class Jarvis():
    def Sir():
        mixer.init()
        mixer.music.load("start.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        
        while True:
            print(Fore.BLUE+"Hello Sir! My Name is JARVIS!")
            time.sleep(10)
            break

    
    def Start():
        engine = pyttsx3.init()
        engine.say('Hello Sir! Whatsup?')
        engine.runAndWait()


    def FIRST_LISTEN():
        def Listen():
            global firstText
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print(Fore.GREEN+"Your Voice Defines…")
                print("\n")
                print(Fore.MAGENTA+"Duration : 5 Second")
                data = r.record(source, duration=5)
                firstText = r.recognize_google(data,language="en")
                print(firstText)
        Listen()
            
        if str(firstText) == "Jarvis" or str(firstText) == "jarvis":
            engine = pyttsx3.init()
            engine.say('Yes Sir?')
            engine.runAndWait()
            print(Fore.GREEN+"I UNDERSTAND YOU SIR!")
            Listen()      
        else:
            engine = pyttsx3.init()
            engine.say("I Don't Understand Sir.")
            engine.runAndWait()
            print(Fore.RED+"I Don't Understand Sir.")
            
            
    # STARTERS
    Sir()
    Start()
    FIRST_LISTEN()
    
jarvis = Jarvis()
