import pyautogui as pi
import time
import subprocess
import pywhatkit as kit
def send_whatsapp():
    # from main import speak
    # from main import take_user_input
    # pi.hotkey('win','up')
    # pi.moveTo(750,1050,1)
    pi.click(x=750, y = 1050, clicks = 1, interval =0, button ='left')
    time.sleep(1)

    pi.typewrite("whatsapp")
    time.sleep(1)
    # pi.moveTo(730,270,1)
    pi.click(x=730, y = 270, clicks = 1, interval =0, button ='left')
    time.sleep(1)

    # print("Do you want to send message to anyone sir? If yes, whom do you want to send?")
    # choice = take_user_input()
    # choice = input("Enter your choice:")
    # if any(keyword in choice.lower() for keyword in ("yes","i need to","search for","can you search","open conversation","open the conversation","i have to","look for","seek for","search for")):
    # pi.moveTo(200,150,1)
    pi.click(x=170, y = 130, clicks = 1, interval =0, button ='left')
    time.sleep(1)
    pi.write("Budi Jaan")
    time.sleep(1)
    # pi.moveTo(200,240)
    pi.click(x=200, y = 240, clicks = 1, interval =0, button ='left')
    time.sleep(1)
    # pi.moveTo(700,990)
    pi.click(x=700, y = 900, clicks = 1, interval =0, button ='left')
    time.sleep(1)
    pi.write("hi")
    pi.press("enter")
    print(f"Message sent.")

    # else:
    #     print("Ok sir.")
    # # pi.typewrite("budi jaan")
    # # time.sleep(1)
    # # pi.click(x=140, y = 460, clicks = 1, interval =0, button ='left')
    # # time.sleep(1)
    # # pi.moveTo(1200,940,0.1)
    # # pi.typewrite("hello")
    # # pi.press('enter')
    # # time.sleep(2)
    # import pywhatkit as kit
    # import time
    # import subprocess
    # # Define contacts as a dictionary
    # contacts = {
    #     "Budi Jaan": "+9779745899005",
    #     "Ishan dost": "+9779840344190",
    #     "Kanxo": "+977",
    #     "bijan mamu": "+85256883120",
    #     "roshan international": "+9779849908831",
    #     "lutee dost": "+9779824076246",
    #     "Tution mam Computer": "+9779841244581",
    # }

    # # Function to open WhatsApp Web
    # def open_whatsapp_web():
    #     name = input("Enter the name of the contact (or type 'exit' to quit): ")
    #     if name.lower() == 'exit':
    #         return None
    #     search_url = 'https://web.whatsapp.com'
    #     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    #     subprocess.Popen([chrome_path, search_url])
    #     time.sleep(12)  # Allow time for WhatsApp Web to load
    #     send_message(name)
    #     time.sleep(10)

    # # Function to send a message

    # def send_message(name):
    #     if name in contacts:
    #         phone_number = contacts[name]
    #         message = f"Hello, this is a test message."
    #         kit.sendwhatmsg_instantly(phone_number, message, 8, True, 1)
    #         print(f"Message sent to {name}.")
    #     else:
    #         print(f"Contact {name} not found in contacts.")

    # # Open WhatsApp Web
    # open_whatsapp_web()

    # # Input loop to send messages to multiple contacts  # Wait a bit before allowing the next message

    # '''c
    # youtube search bar-806,125
    # whatapp search bar- 271,22

# send_whatsapp()