import pyttsx3
import speech_recognition as sr
import pyautogui
import sys
from sketchpy import library as lib



from datetime import datetime
from random import choice
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess as sp
import requests
import wikipedia

import urllib.parse
import webbrowser
import subprocess


#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\myenv\Scripts\Activate

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice', voices[1].id)  # Set voice to female voice



# Set up speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()
# recognizer.energy_threshold = 2000
# Opening text for responses
opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

# Function to greet the user
def greet_user():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        speak("Good morning, sir!")
    elif 12 <= current_hour < 16:
        speak("Good afternoon, sir!")
    elif 16 <= current_hour < 21:
        speak("Good evening, sir!")
    else:
        speak("Hello, sir!")
    speak("I am Jarwis,your virtual assistant. How may I assist you today?")

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def take_user_input():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)
        # audio_data = audio.get_raw_data(convert_rate=44100, convert_width=2)
        # reduced_noise = nr.reduce_noise(audio_data)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print("You said:", query)
        if "open camera" in query.lower() or "camera" in query.lower() or "open the camera" in query.lower():
            open_camera()
            return None
        if "capture photo" in query.lower() or "click photo" in query.lower() or "picture " in query.lower():
            capture_photo()
            return None
        if  "open youtube" in query.lower() or "youtube" in query.lower():
            speak("Sure sir, what would you like to watch on YouTube?")
            query = take_user_input()
            if query == "exit":
                return "exit"
            search_query = extract_search_query(query)
            print("Search query:",search_query)
            search_youtube(search_query)
            return None
        if "open command prompt" in query.lower() or "command prompt" in query.lower() or "command line interface" in query.lower():
            open_cmd()
            return None
        if 'open notepad' in query.lower():
            open_notepad()
            return None
        if "time" in query.lower():
            # current_hour = datetime.now().hour
            strTime = datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is " + strTime)
            return None
        if "cursor" in query.lower() or "eye" in query.lower() or "eyes" in query.lower():
            speak("Ok, sure sir, I am working on it and please keep your eyes infront the camere.")
            eye_cursor_process = sp.Popen(['C:\\Users\\sigde\\OneDrive\\Desktop\\extra python\\myenv\\Scripts\\python.exe', 'C:\\Users\\sigde\\OneDrive\\Desktop\\extra python\\eyecursor.py'])
            eye_cursor_process.wait()
            return None
        if "minimize" in query.lower() or "minimise" in query.lower():
            speak("Ok sir, I am minimizing it.")
            pyautogui.hotkey('win','down','down')
            return None
        if "maximize" in query.lower() or "maximise" in query.lower():
            speak("Ok sir, I am maximizing it.")
            pyautogui.hotkey('win','up','up')
            return None
        if "cloze the window" in query.lower() or "close the window" in query.lower() or "close window" in query.lower() or "close this window" in query.lower():
            speak("Ok sir, I am closing it.")
            pyautogui.hotkey('ctrl','w')
            return None
        if "class routine" in query.lower() or "routine" in query.lower():
            speak("Ok sir, getting your class routine ")
            handle_routine(query)
            return None
        if "draw" in query.lower() or "Tony Stark" in query.lower() or "sketch" in query.lower():
            speak("Drawing sir")
            obj = lib.rdj()
            obj.draw()
            return None
        if "exit" in query.lower() or "stop" in query.lower() or "suta" in query.lower() or "sut" in query.lower() or "sutaa" in query.lower() or "good night" in query.lower():
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
            else:
                speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
            return "exit"
        
            # speak(choice(opening_text))
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service. Please try again to say.")
        return None

def handle_query(query):
    if query is None:
        return None
    query = query.lower()
    common_queries = {
        "how are you":lambda:speak("I am fine sir,thank you for asking and what about you sir."),
        "fuck you":lambda:speak("thank you for your complementary, same to you sir."),
        "fuck you bharat varat ":lambda:speak("yes sir, fuck him fast, fuck you bharat"),
        "who are you":lambda:speak("I am Jarwis, the virtual assistant of Mr. Prabin."),
        "what can you do":lambda:speak("I can perform several tasks like opening youtube,search anything on youtube , google, opening camera, typing, cursor controllingby your eyes or hands , and many more, what do you want me to do?"),
        ("i am bored","bored","feeling bored"):lambda:speak("Ok sir, What can I do for you then? Would you like to watch any videos in youtube?"),
        ("hey jarvis","hi jarvis"):lambda:speak("Yes sir,any command for me?"),
        "chandrama":lambda:speak("Oh, yeah sir, she is your wife. You have married the beautiful girl sir."),
        "bijan":lambda:speak("Oh, yeah I know him sir. He is your student. He feels bored while studying but he loves to play football. You should train him well."),
        "sahil":lambda:speak("Oh, yeah I know him sir. He is your student. He is in A level now. You should train him well."),
        "roshan":lambda:speak("Oh, yeah I got it. The few days ago you checked his bag when you lost your phone. He is really a silly guy sir."),
        ("assam","yasam"):lambda:speak("Oh, yeah I got it. He used to offer you bhola sir."),
        ("sansar","sanchar"):lambda:speak("Oh, yeah I got it. You saved his contact number as hancy hero sir."),
        "ishan":lambda:speak("Oh, yeah I got it. He always seems to come with you while going to college."),
        "hemanta":lambda:speak("Oh, yeah I know him sir, he is principal of Genius school and I think he is pro in smoking."),
        "nikesh":lambda:speak("Yes, of course sir, last time he became famous when he got drunk, he messed up with Abhishek sir too. His profile is in Alpha male group."),
        "sumit":lambda:speak("Oh, yeah I know him sir, he is coordinator of Genius school and I think he loves to dance when he is drunk."),
        "abhishek":lambda:speak("Oh, yes I know him sir, he always uses the word 'muji' when he is drunk, he needs to eat a lot at a single time."),
        "puran":lambda:speak("Oh, yeah I know him sir, he is a sports teacher, he plays basketball well."),
        "rupes":lambda:speak("Oh, yeah I know him sir, he is an accountant in Genius school, he always shakes hands with you when he meets with you.")
    }
    query_lower = query.lower()
    for key, response in common_queries.items():
        if isinstance(key, tuple):
            for k in key:
                if k in query_lower:
                    response()
                    break
        else:
            if key in query_lower:
                response()
    return None

def handle_routine(query):
    if query is None:
        return None
    common_queries = {
        ("sunday","shunday"):lambda:speak("sir, First period will be taken by Prabin sir of E-governance subject, second period will be your practical lab of E-commerce by Abhishek sir, and then third period will also be your lab of Software Engineering by Tek Raj sir, your fourth period will be theory class of dot net by Dharma sir and finally the last one is also the theory session of Technical writing by Keshab sir. And then enjoy sir."),
        ("monday","munday"):lambda:speak("sir, First period will be taken by Prabin sir of E-governance subject, second period will be your practical lab of E-governance again by Prabin sir, and then third period will be your theory of Compiler subject by Ramesh sir, your fourth period will be theory of Software Engineering by Tek Raj sir and finally the last one is also the theory session of Technical writing by Keshab sir. And then enjoy sir."),
        ("tuesday","toesday"):lambda:speak("sir, The first two periods are theory of E-commerce subject by Abhishek sir and E-governance by Prabin sir, and then third period will be lab of Compiler subject by Ramesh sir, your fourth period is also the lab of dot net by Dharma sir and finally the last one is the theory session of Technical writing by Keshab sir. And then enjoy sir."),
        ("wednesday","waynasday","weinesday"):lambda:speak("sir, First theory class will be taken by Prabin Pathak sir of E-governance subject, second period will also be theory of E-commerce by Abhishek sir, and then third period will also be your theory of Software Engineering by Tek Raj sir, your fourth period will be practical of Compiler subject by Ramesh sir and finally the last one is also the theory session of Technical writing by Keshab sir. And then enjoy sir."),
        ("thursday","tustday"):lambda:speak("sir, First period will be your practical lab by Prabin Pathak sir of E-governance subject, second period is also the theory class by Prabin sir, and then third period will also be your theory of Compiler subject by Ramesh sir, your fourth period is again theory class of dot net by Dharma sir and finally hehehe the last one is again the theory session of Technical writing by Keshab sir. And then enjoy sir."),
        ("friday","frayday"):lambda:speak("sir, First period will be taken by Abhishek sir of E-commerce subject, second period will be your practical lab of E-governance by Prabin sir, and then third period will also be your lab of Software Engineering by Tek Raj sir, your both the fourth and fifth period will be theory class of dot net by Dharma sir and Software Engineering by Tek Raj sir. And then enjoy sir."),
        "saturday":lambda:speak("I think you need to remember about the tutions, or futsall program anywhere and if not then enjoy sir"),
    }
    query_lower = query.lower()
    for key, response in common_queries.items():
        if isinstance(key, tuple):
            for k in key:
                if k in query_lower:
                    response()
                    break
        else:
            if key in query_lower:
                response()
    return None
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def capture_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('captured_photo.jpg', image)
    del(camera)
    speak("Photo captured successfully!")
def open_notepad():
    os.system('start notepad')
def open_cmd():
    os.system('start cmd')

def extract_search_query(query):
    start_keywords = ["search ","for","look for", "find", "about","search about","show me","watch"]
    # platform_keywords = ["in youtube", "YouTube", "on youtube", "youtube",]  # Add more platforms as needed
    
    # Split the query into words
    words = query.lower().split()
    
    # Initialize search query
    search_query = ""
    
    # Flag to check if platform keyword is encountered
    # platform_flag = False
    
    # # Iterate over words to extract search query
    for i, word in enumerate(words):
        if word in start_keywords:
            search_query = " ".join(words[i + 1:])
            # Start of search query found
            # search_query = " ".join(words).replace(word, "", 1).strip()
        # elif word in platform_keywords:
        #     platform_index = words.index(word)
        #     if platform_index < len(words) - 1:
        #     # # Combine the words after the platform keyword
        #        search_query = " ".join(words[:platform_index + 1])
        #     else:
        #         search_query = " ".join(words[i + 1:])
    
    return search_query
    # return search_query.strip()


def search_youtube(search_query):
    try:
        speak(",Okay sir,I am working for it.")
        base_url = "https://www.youtube.com/results?search_query="
        query_encoded = urllib.parse.quote(search_query)
        search_url = base_url + query_encoded
        webbrowser.open(search_url)
    except sr.RequestError:
        speak("Sorry, I can't perform this action right now")
    except Exception as e:
        print("An error occurred:", e)

# Main function to execute the program
def main():
    greet_user()
    while True:
        user_input = take_user_input()
        if user_input == "exit":  
            break
        handle_query(user_input)
        
    

if __name__ == "__main__":
    try:
        import pywhatkit as kit
        main()
    except Exception as e:# ImportError:
        speak("Pywhatkit is not available. Running without it. We are not using any internet connections.")
        main()
   

#hello world





