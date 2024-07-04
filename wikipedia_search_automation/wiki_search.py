import wikipedia

def extract_search_Query(query):
        # from main import speak
        start_keywords = ["search","for","look for","find","find that","about","search about","tell me","that","answer of","question","questions"]
        # Split the query into words
        future_query = query
        words = query.split()
        # Initialize search query
        search_query = ""
        # # Iterate over words to extract search query
        for i, word in enumerate(words):
            if word in start_keywords:
                search_query = " ".join(words[i + 1:])
        if search_query == "":
            search_query = future_query
        get_wikipedia_summary(search_query)
def get_wikipedia_summary(query):
    from main import speak
    try:
        results = wikipedia.summary(query,sentences=3)
        speak("According to wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        speak("Unable to find from wikipedia sir, can you modify your question pattern again?")



            


