import pywhatkit as kit

def search_google(query):
        from main import speak
        start_keywords = ["search ","for","look for", "find", "about","search about","show me","watch"]
        words = query.lower().split()
        query = ""
        for i, word in enumerate(words):
            if word in start_keywords:
                query = " ".join(words[i + 1:])
        

        # end_keywords = ["in google", "gogle", "on google", "google","in the google","on the google"]
        # words = query.lower().split()
        # query = ""
        # for i, word in enumerate(words):
        #     if word in end_keywords:
        #         query = " ".join(words[:i + 1])
                
        kit.search(query)
        speak("Ok sir, here is your search result.")