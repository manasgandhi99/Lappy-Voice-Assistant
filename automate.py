import speech_recognition as sr
import pyttsx as pys
import engineio
import datetime
import wikipedia
import os
import webbrowser
from movie import *

engineio = pys.init()
engineio.setProperty('rate', 150)    
voices = engineio.getProperty('voices')
engineio.setProperty('voice',voices[1].id)
volume = engineio.getProperty('volume') 
engineio.setProperty('volume',1.0)

#speak func to speakout audio
def speak(audio):
    engineio.say(audio)
    engineio.runAndWait()

#bot says opening words
def greet():
    now = int(datetime.datetime.now().hour)
    print(now)

    if now>=0 and now<12:
        speak("Good Morning , waddup waddup??")
    if now>=12 and now<18:
        speak("Good Afternoon , waddup waddup??")
    if now>=18 and now<24:
        speak("Good Evening , waddup waddup??")
    
    # speak("How may I help you friend ?")

#bot will take the specific command
def Command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        
        try:
            instruction = r.recognize_google(audio)
            print(instruction)
            return instruction.lower()
        except sr.UnknownValueError:
            print("Error")
            return None
        except sr.RequestError as e:
            print(e)
            return None

# greet()

c = 0 
while True:
    print("Start")
    def main():
        instruction = Command()

        if "wikipedia" in instruction.lower():
            speak("Searching Wikipedia..")
            inst = instruction.replace("wikipedia","")
            results = wikipedia.summary(inst,sentences=2)
            print(results)
            speak(results)

        if "open youtube" in instruction.lower():
            speak("Opening youtube")
            webbrowser.open("www.youtube.com")
        
        

        if "movie review" in instruction.lower():
            speak("what is the name of the movie?")
            r1 = sr.Recognizer()

            with sr.Microphone() as source:
                audio = r1.listen(source)
                
                try:
                    review = r1.recognize_google(audio)
                    print(review)
                    bot = Movie()
                    rating = bot.movie_review(review)
                    speak("The IMDB rating of this movie is" + rating)
                except sr.UnknownValueError:
                    print("Error")
                except sr.RequestError as e:
                    print(e)


        elif "close" in instruction:
            exit()

        elif "open youtube" or "wikipedia" or  "close" or "movie review" not in instruction:
            speak("I could not get an instruction to perform")
    
    if(c>0):
        speak("What should I do next?")

    main()
    c = c + 1


#getting info from wiki


