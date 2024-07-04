
def handle_routine(query):
        from main import speak
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

    