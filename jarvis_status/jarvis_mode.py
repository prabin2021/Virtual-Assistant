
def toggle_jarwis_mode(mode):
        from main import speak
        global listening
        global c
        if mode == "sleep":
            listening = False
            speak("Now I will be in sleeping mode. I won't listen to any commands.")
        elif mode == "wake up":
            listening = True
            c = 0
            speak("I am now awake. Welcome back sir.")
        elif mode == "noaction":
             listening = False