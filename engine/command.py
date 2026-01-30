import pyttsx3
import speech_recognition as sr
import eel



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174) 
    print(voices) 
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()

    except Exception as e:
        return ""
    
    return query.lower()

# text = takecommand()

# speak(text)

@eel.expose
def allCommands():
    query = takecommand()
    print(query)
    