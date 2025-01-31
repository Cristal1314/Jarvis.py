from blinker import receiver_connected
import pyttsx3 #pip install pyttsx3 == it is used to convert text to speech
import datetime
from service_identity import SubjectAltNameWarning
import speech_recognition as sr
import smtplib
from secrets_1 import senderemail, epwd, to
from email.message import EmailMessage
# import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia

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
    with sr.Microphone() as source:
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

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content()
    server.send_message(email)
    server.sendEmail(senderemail, to,content)
    server.close()

sendEmail()

def searchgoogle():
    speak('What should I search for?')
    search = takeCommandMIC()
    wb.open("https://www.google.co.uk/?safe=active&ssui=on")

if __name__ == "__main__":
    # getvoices(1)
    wishme()
    while True:
        query = takeCommandCMD().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
while True:
    query = takeCommandMIC().lower()
    if 'time' in query:
        time()
    elif 'date' in query:
        date()
    elif 'email' in query:
        email_list = {
            'testemail': 'itzanxkqrofhfrgwfn@kiabws.com'
        }
        try:
            speak("To whom you want to send the email?")
            name = takeCommandMIC
            receiver = email_list[name]
            speak("what is the subject of the mail?")
            subject = takeCommandCMD
            speak('what should I say?')
            content = takeCommandMIC()
            sendEmail(receiver,subject,content)
            speak('email has been send')
        except Exception as e:
            print(e)
            speak("unable to end email")
    elif 'offline' in query:
         quit()

    elif 'wikipedia' in query:
        speak('searching on wikipedia')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences = 2)
        print(result)
        speak(result)
    
    elif 'search' in query:
        searchgoogle()
    
    elif 'offline' in query:
        quit()


#-----------------------------------Send Email Function------------------------------------------