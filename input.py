import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    #Converts text to speech
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    #Greets the user based on the time of day.
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")
    
    else:
        speak("Good Evening")

    speak("Hello I am Siza your voice assistant. How may I help you")

def calculate(expression):
    #calcualte expression
    try:
        result = eval(expression)
        print("Result:", result)
        speak(f"The result is {result}")
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")

def takeCommand():
    #Listens for a command from the user via the microphone
    #and returns the recognized text.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
     query=takeCommand().lower()

     #logic for executing tasks based on query
     if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
     elif 'open youtube' in query:
            webbrowser.open("youtube.com")
     elif 'open google' in query:
            webbrowser.open("google.com")
     elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com") 

     elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, the time is {strTime}")

     elif 'play music' in query:
            music_dir='C:\\Users\\hp\\OneDrive\\Desktop\\music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
    
     elif 'open vs code' in query:
            codepath= 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(codepath)

     elif 'calculate' in query:
            print("Please tell me the expression:")
            speak("Please tell me the expression")
            expression = takeCommand()
            calculate(expression)

     elif 'exit' in query or 'stop' in query:
             speak("Goodbye!")
             break
            
          