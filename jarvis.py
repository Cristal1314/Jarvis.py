import pyttsx3 #pip install pyttsx3 == it is used to convert text to speech
import datetime
import speech_recognition as sr
import smtplib
from secrets import senderemail, epwd, to 
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# while True:
#     text = input("Enter some text to convert into speech")
#     speak(text)
#---------------------------------Time + Date Function--------------------------------------------------
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # Hour = I, Min = M, Sec = S
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is: ")
    speak(date)
    speak(month)
    speak(year)

date()
#-----------------------------------------Greeting and Wish me function--------------------------------------------

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Eveing Sir!")
    else:
        speak("Good Night Sir!")

greeting()

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how can I help you?")

wishme()

#-----------------------------------User input From CMD(text input)/Mic(Audio input)-----------------------------

def takeCommandCMD():
    query = input("please tell me how can I help you?\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("User Said : "+query)
    except Exception as e:
        print(e)
        speak("Say that Again Please....")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandCMD().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'email' in query:
            try:
                speak('what should I say?')
                content = takeCommandMIC()
                senderemail(content)
                speak('email has been send')
            except Exception as e:
                print(e)
            speak("unable to end email")
        elif 'offline' in query:
            quit()

#-----------------------------------Send Email Function---------------------------------------------------------
def sendEmail():
    server = smtplib.SMIP('smtp.gamil.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    server.sendermail(senderemail, to, 'hello this is a test email by jarvis')
    server.close()

sendEmail()