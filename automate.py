import speech_recognition as sr
import pyttsx as pys
import engineio
import datetime
import wikipedia
import os
import webbrowser
import time
from utils import *
from movie import *
from youtube import *
from sendemail import *
from google import  *
from note import *
from whatsapp import *

#bot says opening words
def greet():
    now = int(datetime.datetime.now().hour)
    # print(now)

    if now>=0 and now<12:
        speak("Good Morning , waddup waddup??")
    if now>=12 and now<18:
        speak("Good Afternoon , waddup waddup??")
    if now>=18 and now<24:
        speak("Good Evening , waddup waddup??")     
    
    # speak("How may I help you friend ?")

greet()
time.sleep(2)
#bot starts taking commands
c = 0 
WAKE  = "Bonjo"
print("Start")

while True:
    inst = Command()

    if inst.count(WAKE.lower()) > 0:
        speak("I am ready!")
        inst = Command()

        def main(query):
            if query!= None :
                instruction = query
            else :
                instruction = Command()
            
            wiki = ["open in wikipedia","browse in wikipedia","search in wikipedia"]
            for words in wiki :
                if words in instruction:
                    speak("Searching Wikipedia..")
                    inst = instruction.replace("wikipedia","")
                    results = wikipedia.summary(inst,sentences=2)
                    print(results)
                    speak(results)
                    main(None)
                    break

            you = ["open youtube","browse in youtube","watch a video","look for a video"]
            for words in you :
                if words in instruction:
                    speak("Opening youtube..")
                    bot = Youtube()
                    query = bot.play()
                    main(query)
                    break

            mov = ["movie review","imdb rating","movie rating"]
            for words in mov :
                if words in instruction:
                    speak("what is the name of the movie?")
                    review = Command()
                    bot = Movie()
                    rating = bot.movie_review(review)
                    if rating != None:
                        speak("The IMDB rating of this movie is" + rating)
                    else:
                        speak("The IMDB rating for this movie is not available")
                    main(None)
                    break
            
            gog = ["open google","browse in google","search in google","open browser"]
            for words in gog :
                if "open google" in instruction:
                    speak("Opening Google..")
                    speak("What should I search for?")
                    text = Command()
                    Google.search(text)
                    break
            
            aud = ["save my audio","take my audio","store my audio"]
            for words in aud :
                if words in instruction:
                    speak("What audio is to be saved?")
                    audio = Command()
                    saveVoice(audio)
                    break
            
            cod = ["open vscode","open my favourite ide","open new code file"]
            for words in cod :
                if words in instruction:
                    speak("Opening Code..")
                    codePath = "C:\\Users\\Jiten\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                    os.startfile(codePath)
                    main(None)
                    break
            
            ema = ["send email","write an email","send mail"]
            for words in ema :
                if words in instruction:
                    try:
                        speak("What is the reciever's email address?")
                        to = Command()
                        speak("What should I send?")
                        content = Command()
                        # to = "example@gmail.com"
                        sendEmail.send(to,content)
                        speak("Email sent successfully!")
                        print("email sent!")
                    except Exception as e:
                        print("Error : ",e)
                    main(None)
                    break

            notes = ["take a note","note this","open notepad"]
            for words in notes :
                if words in instruction:
                    speak("Opening Notepad..")
                    speak("What should I note?")
                    text = Command()
                    Notepad.note(text)
                    main(None)
                    break
            
            wha = ["text him","text her","message him","send a message","message her"]
            for words in wha :
                if words in instruction:
                    speak("Opening Whatsapp..")
                    speak("What is the name of the contact on Whatsapp?")
                    to = Command()
                    speak("What message should I send?")
                    message = Command()
                    com = Whatsapp.msg(to,message)
                    main(com)
                    break

            clo = ["close it","bye","turn off","shut up"]
            for words in clo :
                if words in instruction:
                    speak("Pleasure talking to you.....Byee....Have a nice day!!")
                    exit()

        # elif "open youtube" or "wikipedia" or  "close" or "movie review" not in instruction:
        #     speak("I could not get an instruction to perform")
    
        if(c>0):
            speak("What should I do next?")
            main(None)
        
        main(inst)
        c = c + 1




