from basic_functions.basic_functionalities import *
from battery_status.battery_check import *
from camera_automation.open_camera import *
from email_automation.send_email import *
from google_automation.google_search import *
from greetings.greeting import *
from jarvis_status.jarvis_mode import *
from joke.jokes_teller import *
from queries_handling_functions.query_handle import *
from routine_handling.routine_sayer import *
from sentiment_analyzer.sentiment_analyze import *
from youtube_automation.search_on_youtube import *
from data_required.dialogues import *
from wikipedia_search_automation.wiki_search import *

import pyttsx3
import speech_recognition as sr
import pyautogui
import urllib.parse
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess as sp
import cv2
import smtplib
import tkinter as tk
import pywhatkit as kit
import webbrowser
from datetime import datetime
from sketchpy import library as lib
from random import choice
from PIL import Image, ImageTk
import requests
import wikipedia
import sys
import subprocess
from mtranslate import translate
from colorama import Fore,Style,init
import threading
import psutil
import re
from transformers import pipeline
import logging
import time


# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)

engine.setProperty('voice', voices[1].id)  # Set voice to female voice
logging.basicConfig(level=logging.INFO)
listening = True
recognizer = sr.Recognizer()
microphone = sr.Microphone()
sentiment_checked = False
c=0



def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_user_input():
    global listening
    global c
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        recognizer.energy_threshold = 250
        audio = recognizer.listen(source,0,10)

        # audio_data = audio.get_raw_data(convert_rate=44100, convert_width=2)
        # reduced_noise = nr.reduce_noise(audio_data)
    query = None
    try:
        print("Trying to recognize as Nepali language...")
        query1 = recognizer.recognize_google(audio, language="ne")
        query_translated = translate(query1,to_language="en")
        print("You said:", query_translated)
        query = query_translated.lower()
    except sr.UnknownValueError:
        try:
            print("Trying to recognize as English language...")
            query1 = recognizer.recognize_google(audio, language="en")
            query= query1.lower()
            print("You said:", query)
        except sr.UnknownValueError:
            print("Unable to recognize...")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service. Please try again.")
            return None
    if not query:
        return None
    elif not listening:
        if "jarvis wake up" in query or "wake up" in query or "wakeup" in query:
            print("Wake up command detected")
            toggle_jarwis_mode("wake up")
        else:
            print("Jarvis is sleeping. Discarding command.")
        return None
    elif "jarvis sleep" in query or "sleep for a while" in query:
        toggle_jarwis_mode("sleep")
        return None
   
    

    else:
        # handle_query(query)
        # process_command(query)
        return query

 
def process_command(query):   
    global sentiment_checked 
    if not sentiment_checked:
        sentiment, confidence = analyze_sentiment(query)
        print(f"Your Sentiment: {sentiment}, Your Confidence: {confidence:.2f}")
        if sentiment == 'NEGATIVE' and confidence > 0.7:
            speak("I sense some negativity in your voice. Is everything alright sir?")
        sentiment_checked = True

    if "open camera" in query or "camera" in query or "open the camera" in query:
        open_camera()
        return None
    if "capture my photo" in query or "click my photo" in query or "picture " in query:
        capture_photo()
        return None
    if  "open youtube" in query or "youtube" in query:
        speak("Sure sir, what would you like to watch on YouTube?")
        query = take_user_input()
        if query == "exit":
            return 
        search_query = extract_search_query(query)
        print("Search query:",search_query)
        search_youtube(search_query)
        return None
    if "open command prompt" in query or "command prompt" in query or "command line interface" in query:
        open_cmd()
        return None
    if 'open notepad' in query:
        open_notepad()
        return None
    if "time" in query:
        # current_hour = datetime.now().hour
        strTime = datetime.now().strftime("%H:%M:%S")
        speak("Sir, the time is " + strTime)
        return None
    if "cursor" in query or "eye" in query or "eyes" in query:
        speak("Ok, sure sir, I am working on it and please keep your eyes in front of the camera.")
        try:
            sp.run(['python','D:\\Environments\\eyecursor.py'])
        except FileNotFoundError:
            print("Error: The eyecursor.py script was not found.")
        except sp.CalledProcessError as e:
            print("Error executing eyecursor.py:", e)
    if "minimize" in query or "minimise" in query:
        speak("Ok sir, I am minimizing it.")
        pyautogui.hotkey('win','down','down')
        return None
    if "maximize" in query or "maximise" in query:
        speak("Ok sir, I am maximizing it.")
        pyautogui.hotkey('win','up','up')
        return None
    if "cloze the window" in query or "close the window" in query or "close window" in query or "close this window" in query:
        speak("Ok sir, I am closing it.")
        pyautogui.hotkey('ctrl','w')
        return None
    if "class routine" in query or "routine" in query:
        speak("Ok sir, getting your class routine ")
        handle_routine(query)
        return None
    if "draw" in query or "Tony Stark" in query or "sketch" in query:
        speak("Drawing sir")
        obj = lib.rdj()
        obj.draw()
        return None
    if  "greet me" in query or "greet" in query:
        greet_user()
        return None
    if  "send mail" in query or "send an email" in query or "send email" in query or "send e-mail" in query or "send the email" in query:
        result_email = send_email()
        return result_email

    if "check battery percentage" in query or "battery percentage" in query or "battery status" in query or "check the battery percentage" in query:
        battey_persentage()

    if "search for" in query or "search in google" in query or "google" in query:
        search_google(query)
        return None
    if  "use wikipedia" in query or "wikipedia" in query:
        speak("Sure sir, what would you like to search for?")
        query = take_user_input()
        if query == "exit":
            return 
        extract_search_Query(query)
        return None
    if "exit" in query or "stop" in query or "quit" in query or "good night" in query:
        current_hour = datetime.now().hour
        if current_hour >= 21 or current_hour < 6:
            speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
        else:
            speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
        return "exit"
    
# Main function to execute the program
def main():
    greet_user()
    while True:
        user_input = take_user_input()
        if user_input:
            result = handle_query(user_input)
            result = process_command(user_input)
            if result == "exit":  
                break
            # handle_routine(user_input)
        else:
            
            continue

if __name__ == "__main__":
        main()
   







