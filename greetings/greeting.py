from datetime import datetime
import random
def greet_user():
        from main import speak
        from data_required.dialogues import good_afternoon_dlg,good_evening_dlg,good_morning_dlg,good_night_dlg

        current_hour = datetime.now().hour
        if 1 <= current_hour < 12:
            speak(random.choice(good_morning_dlg))
        elif 12 <= current_hour < 16:
            speak(random.choice(good_afternoon_dlg))
        elif 16 <= current_hour < 21:
            speak(random.choice(good_evening_dlg))
        else:
            speak("Hello, sir! I am Jarwis,your virtual assistant. How may I assist you today?")