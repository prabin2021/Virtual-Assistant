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
import random




#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\myenv\Scripts\Activate

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice', voices[1].id)  # Set voice to female voice


listening = True
# Set up speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()
# recognizer.energy_threshold = 2000
# Opening text for responses
# opening_text = [
#     "Cool, I'm on it sir.",
#     "Okay sir, I'm working on it.",
#     "Just a second sir.",
# ]

# Function to greet the user

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def take_user_input():
    global listening
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)
        # audio_data = audio.get_raw_data(convert_rate=44100, convert_width=2)
        # reduced_noise = nr.reduce_noise(audio_data)
    query = None
    try:
        print("Trying to recognize as Nepali language...")
        query1 = recognizer.recognize_google(audio, language="ne")
        query_translated = translate(query1,to_language="en")
        print("You said:", query_translated)
        query = query_translated
    except sr.UnknownValueError:
        try:
            print("Trying to recognize as English language...")
            query1 = recognizer.recognize_google(audio, language="en")
            query= query1
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
        if "jarvis wake up" in query.lower() or "wake up" in query.lower() or "wakeup" in query.lower():
            print("Wake up command detected")
            toggle_jarwis_mode("wake up")
        else:
            print("Jarvis is sleeping. Discarding command.")
        return None
    elif "jarvis sleep" in query.lower() or "sleep for a while" in query.lower():
        toggle_jarwis_mode("sleep")
        return None
    else:
        process_command(query)
        return query
        
def process_command(query):   
    if "open camera" in query.lower() or "camera" in query.lower() or "open the camera" in query.lower():
        open_camera()
        return None
    if "capture my photo" in query.lower() or "click my photo" in query.lower() or "picture " in query.lower():
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
        speak("Ok, sure sir, I am working on it and please keep your eyes in front of the camera.")
        try:
            sp.run(['python','D:\\Environments\\eyecursor.py'])
        except FileNotFoundError:
            print("Error: The eyecursor.py script was not found.")
        except sp.CalledProcessError as e:
            print("Error executing eyecursor.py:", e)
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
    if  "greet me" in query.lower() or "greet" in query.lower():
        greet_user()
        return None
    if  "send mail" in query.lower() or "send an email" in query.lower() or "send email" in query.lower() or "send e-mail" in query.lower():
        result_email = send_email()
        return result_email

    if "check battery percentage" in query.lower() or "battery percentage" in query.lower() or "battery status" in query.lower() or "check the battery percentage" in query.lower():
        battey_persentage()
    if "check plug" in query.lower() or "check battery plug" in query.lower():
        check_plugin_status1()
    if "give me the battery alert" in query.lower() or "battery alert" in query.lower():
        battery_alert1()


    if "exit" in query.lower() or "stop" in query.lower() or "quit" in query.lower() or "good night" in query.lower():
        current_hour = datetime.now().hour
        if current_hour >= 21 or current_hour < 6:
            speak("Good night, sir. Take care!, and please wake me up when you feel bored or if any help needed.")
        else:
            speak("Have a good day, sir!, and please wake me up when you feel bored or if any help needed.")
        return "exit"


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


def handle_query(query):
    if query is None:
        return None
    # query = query.lower()
    common_queries = {
        "how are you":lambda:speak("I am fine sir,thank you for asking and what about you sir."),
        "fuck you bro ":lambda:speak("thank you for your complementary, same to you sir."),
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
        "rupes":lambda:speak("Oh, yeah I know him sir, he is an accountant in Genius school, he always shakes hands with you when he meets with you."),
        "kevin":lambda:speak("Oh, yeah I know him sir, he is your student, he is currently in A level"),
        ("kevin hero"):lambda:speak("kevin is hero sir")
        
    }
    # query_lower = query.lower()
    # for key, response in common_queries.items():
    #     if key == query_lower:  # Check for exact match
    #         response()
    #         return  # Stop processing further queries
    #     elif isinstance(key, tuple) or query_lower in key:  # Check for partial match within tuple
    #         response()
    #         return  # Stop processing further queries
    # return None
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

def toggle_jarwis_mode(mode):
    global listening
    if mode == "sleep":
        listening = False
        speak("I am now sleeping. I won't listen to any commands.")
    elif mode == "wake up":
        listening = True
        speak("I am now awake. I'm listening again.")

def search_youtube(search_query):
    try:
        speak(",Okay sir,I am working for it.")
        base_url = "https://www.youtube.com/results?search_query="
        query_encoded = urllib.parse.quote(search_query)
        search_url = base_url + query_encoded
        # webbrowser.open(search_url)
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        subprocess.Popen([chrome_path, search_url])
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

# def send_email():
#     try:
#         speak("Sure sir. Please provide the recipient's email address.")
#         speak("How would you like to provide recipient's email address?")
#         choice_in_email  = take_user_input()
#         if "voice" in choice_in_email.lower() or "say" in choice_in_email.lower():
#             recipient_email = take_user_input()
#             if recipient_email:
#                 recipient_email = recipient_email.replace(" ", "")
#             print(recipient_email)
#         elif "type" in choice_in_email.lower() or "write" in choice_in_email.lower():
#             recipient_email = input("Recipient's Email Address: ")
#         speak("What is the subject of the email?")
#         subject = take_user_input()
#         if "exit" in subject.lower():
#             return "exit"
#         speak("Please dictate the message content.")
#         message_content = take_user_input()
#         if "exit" in message_content.lower():
#             return "exit"

#         # Your email credentials and SMTP server details
#         sender_email = "sigdelprabin321@gmail.com"
#         ohoo = "omet osmk kavu tlrw"
#         smtp_server = "smtp.gmail.com"
#         smtp_port = 587  # or 465 for SSL

#         # Create MIMEMultipart message
#         message = MIMEMultipart()
#         message['From'] = sender_email
#         message['To'] = recipient_email
#         message['Subject'] = subject

#         # Attach message content
#         message.attach(MIMEText(message_content, 'plain'))

#         # Attachment functionality
#         speak("Do you have anything to attach here sir ?")
#         attach_choice = take_user_input()

#         if 'yes' in attach_choice.lower() or 'yeah' in attach_choice.lower() or 'offcourse' in attach_choice.lower():
#             speak("Please provide the file path sir")
#             file_path = input("Enter your file path:\n")

#             if os.path.exists(file_path):
#                 # Open the file in binary mode
#                 with open(file_path, 'rb') as attachment:
#                     # Add file as application/octet-stream
#                     # Email client can usually download this automatically as attachment
#                     part = MIMEBase('application', 'octet-stream')
#                     part.set_payload(attachment.read())

#                 # Encode file in ASCII characters to send via email
#                 encoders.encode_base64(part)
#                 # Add header as key/value pair to attachment part
#                 part.add_header(
#                     'Content-Disposition',
#                     f'attachment; filename= {os.path.basename(file_path)}'
#                 )
#                 # Add attachment to message and convert message to string
#                 message.attach(part)
#             else:
#                 speak("File not found. Attachment skipped.")



#         # Create SMTP server connection
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # Secure the connection
#         server.login(sender_email, ohoo)  # Login to your email account

#         # Construct the email message
#         email_message = f"Subject: {subject}\n\n{message_content}"

#         speak("Please confirm the email content. Subject: {}. Message: {}. Do you want to proceed? (Yes or No)".format(subject, message_content))
#         confirm = take_user_input()

#         if confirm.lower() != 'yes':
#             speak("Email sending cancelled.")
#             return
#         # Send the email
#         server.sendmail(sender_email, recipient_email, email_message)

#         # Close the SMTP server connection
#         server.quit()

#         speak("Sir, Email is send successfully!")
#     except Exception as e:
#         print("An error occurred while sending the email:", e)
#         speak("Sorry, I couldn't send the email. Please try again.")
    


def send_email():
    try:
        speak("Sure sir. I need recipient's email address.")
        speak("How would you like to provide recipient's email address?")
        choice_in_recipient = take_user_input()

        if "voice" in choice_in_recipient.lower() or "say" in choice_in_recipient.lower() or "tell" in choice_in_recipient.lower():
            print("Recipient address: ")
            recipient_email = take_user_input()
            recipient_email = recipient_email.strip().lower()
            recipient_email = recipient_email.replace(" ", "")
            print("Recipient address: ", recipient_email)
        elif "type" in choice_in_recipient.lower() or "write" in choice_in_recipient.lower():
            recipient_email = input("Recipient's Email Address: ")
            print("Recipient address: ", recipient_email)

        speak("I need subject of your email.")
        speak("How would you like to provide subject?")
        choice_in_subject = take_user_input()
        if "voice" in choice_in_subject.lower() or "say" in choice_in_subject.lower() or "tell" in choice_in_subject.lower():
            subject =  take_user_input()
            print("Subject: ", subject)
            if "exit" in subject.lower():
                return 
        elif "type" in choice_in_subject.lower() or "write" in choice_in_subject.lower():
            subject = input("Write your subject: ")
            print("Subject: ", subject)
            if "exit" in subject.lower():
                return 

        speak("How will you provide me the message sir?")
        choice_in_message = take_user_input()
        if "voice" in choice_in_message.lower() or "say" in choice_in_message.lower() or "tell" in choice_in_message.lower():
            message =  take_user_input()
            print("Message: ", message)
            if "exit" in message.lower():
                return 
        elif "type" in choice_in_message.lower() or "write" in choice_in_message.lower():
            message = input("Write your message: ")
            print("Message: ", message)
            if "exit" in message.lower():
                return 

        # Your email credentials and SMTP server details
        sender_email = "sigdelprabin321@gmail.com"
        
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # or 465 for SSL
        ohoo = "omet osmk kavu tlrw"

        # Create MIMEMultipart message
        message_content = MIMEMultipart()
        message_content['From'] = sender_email
        message_content['To'] = recipient_email
        message_content['Subject'] = subject

        # Attach message content
        message_content.attach(MIMEText(message, 'plain'))

        # Attachment functionality
        speak("Do you have anything to attach here sir ?")
        attach_choice = take_user_input()

        if 'yes' in attach_choice.lower() or 'yeah' in attach_choice.lower() or 'offcourse' in attach_choice.lower() or 'of course' in attach_choice.lower():
            print("Please provide the file path sir")
            file_path = input("Enter your file path:\n")

            if os.path.exists(file_path):
                # Open the file in binary mode
                with open(file_path, 'rb') as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())

                # Encode file in ASCII characters to send via email
                encoders.encode_base64(part)
                # Add header as key/value pair to attachment part
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(file_path)}'
                )
                # Add attachment to message and convert message to string
                message_content.attach(part)
            else:
                print("File not found. Attachment skipped.")

        # Create SMTP server connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, ohoo)  # Login to your email account

        # Construct the email message
        email_message = message_content.as_string()

        speak("Please confirm the email content. Subject: {}. Message: {}. Do you want to proceed? (Yes or No)".format(subject, message))
        confirm = take_user_input()

        if ['yes', 'yeah', 'of course', 'offcourse','okay','sure','done'] in confirm.lower():
            server.sendmail(sender_email, recipient_email, email_message)
            server.quit()
            print("Sir, Email is sent successfully!")
        else:
            print("Email sending cancelled.")

    except Exception as e:
        print("An error occurred while sending the email:", e)
        print("Sorry, I couldn't send the email. Please try again.")


def battery_alert1():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            speak(f"Your battery is less than 30 percent,You have only {percent} percent sir.")

        elif percent < 10:
            speak(f"Your battery is less than 10 percent,You have only {percent} percent sir.")

        elif percent == 100:
            speak(f"Your battery is fully charged,You have {percent} percent sir.")
        else:
            speak(f"sir,your battery is in perfect battery level, you have {percent} percent sir.")

previous_state = None
def check_plugin_status1():
    global previous_state  # Use the global variable

    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            speak("Charger is plugged in")
        else:
            speak("Charger is plugged out")
        previous_state = battery.power_plugged
    return None


def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speak(f"the device is running on {percent}% battery power")
    secsleft = battery.secsleft
    if secsleft == psutil.POWER_TIME_UNLIMITED:
        speak("Battery is fully charged.")
    elif secsleft == psutil.POWER_TIME_UNKNOWN:
        speak("Battery time left is unknown.")
    else:
        hours, remainder = divmod(secsleft, 3600)
        minutes, _ = divmod(remainder, 60)
        time_left_message = f"if you normally use your device then you will be able to use about: {hours} hours and {minutes} minutes sir."
        speak(time_left_message)
    return None


if __name__ == "__main__":
    try:
        import pywhatkit as kit
        main()
    except Exception as e:# ImportError:
        speak("Pywhatkit is not available. Running without it. We are not using any internet connections.")
        main()
   







