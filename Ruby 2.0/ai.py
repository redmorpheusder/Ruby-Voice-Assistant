import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pyaudio
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from tkinter import*
from tkinter import messagebox






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

quit = False
botname =("Ruby")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>= 4 and hour<12:
        speak("Good Morning User!")
        print()
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon User!")  
        print("Good Afternoon User!")
    else:
        speak("Good Evening User!") 
        print("Good Afternoon User!")

    speak("How I can help you?")
    print("How I can help you?")






def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    global sentence
    global flag_rec
    flag_rec = True

    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            sentence=r.recognize_google(audio)
            print(sentence.capitalize())
        except sr.UnknownValueError:
            speak("Sorry I didnt understand")
            print("Sorry I didnt understand")
            flag_rec=False

        except sr.RequestError:
            speak("Error on a server!")
            flag_rec=False

   



if __name__ == '__main__':
    greetings()

    while quit != True:
        listen()


        if flag_rec == False:
            sentence = "Mr.Saxobeat"
            continue

        if "search" in sentence or "what is" in sentence:
            sentence.replace("search","")
            sentence.replace("what is","")
            speak("According to Wikipedia")
            print("According to Wikipedia:")
            search = wikipedia.summary(sentence, sentences = 3)
            print(search)
            speak(search)

        elif "your name" in sentence or "call you" in sentence: 
            print("I am",botname)
            speak("I am ")
            speak(botname)
       


        elif "goodbye" in sentence or "bye" in sentence:
            print("Goodbye User!")
            speak("Goodbye User!")     
            quit = True
       

        elif "joke" in sentence:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)  
            



    
        
        


