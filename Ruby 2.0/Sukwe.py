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


class Window(Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master

        self.pack()

        master.title("Ruby")

        A = Label(master, text="Here to serve you!",)
        A.configure(font='gothic 13')

        A.pack(side="top")

        Button(master, text="Give Command", bg="red", width=100,relief="groove",command=self.Processo_r).pack(side="bottom")

    
        

        
        
    def Processo_r(self):

        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        quit = False
        botname =("Ruby")
        


        #Greetings to user 
        

        engine.say("How I can help you?")
        engine.runAndWait()
        print("How I can help you?")


        #Listening
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
            engine.say("Sorry I didnt understand")
            engine.runAndWait()
            print("Sorry I didnt understand")
            flag_rec=False

        except sr.RequestError:
            engine.say("Error on a server!")
            engine.runAndWait()
            flag_rec=False






        if flag_rec == False:
             sentence = "Mr.Saxobeat"

        if "search" in sentence or "what is" in sentence:
            sentence.replace("search","")
            sentence.replace("what is","")
            engine.say("According to Wikipedia")
            engine.runAndWait()
            print("According to Wikipedia:")
            search = wikipedia.summary(sentence, sentences = 3)
            print(search)
            engine.say(search)
            engine.runAndWait()

        elif "your name" in sentence or "call you" in sentence: 
            print("I am",botname)
            engine.say("I am ")
            engine.runAndWait()
            engine.say(botname)
            engine.runAndWait()
       


        elif "goodbye" in sentence or "bye" in sentence:
            print("Goodbye User!")
            engine.say("Goodbye User!") 
            engine.runAndWait()
            quit = True
            exit()
       

        elif "joke" in sentence:
            joke = pyjokes.get_joke()
            print(joke)
            engine.say(joke)
            engine.runAndWait()


        elif "time" in sentence:
            hour = int(datetime.datetime.now().hour)
            engine.say("It is ")
            engine.runAndWait()
            engine.say(hour)
            engine.runAndWait()
            engine.say("o clock ")
            engine.runAndWait()


        elif "hello" in sentence or "hi" in sentence:
            hour = int(datetime.datetime.now().hour)
            if hour>= 4 and hour<12:
                engine.say("Good Morning User!")
                engine.runAndWait()
                print()
  
            elif hour>= 12 and hour<18:
                engine.say("Good Afternoon User!") 
                engine.runAndWait()
                print("Good Afternoon User!")
            else:
                sengine.say("Good Evening User!") 
                engine.runAndWait()
                print("Good Afternoon User!")


        elif "how are you" in sentence:
            engine.say("Am doing great! Thanks")
            engine.runAndWait()

           



root = Tk()

#instance of the class

app = Window(root)

root.geometry("1000x100")

#Runs the application until we close

root.mainloop()