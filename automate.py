import speech_recognition as sr
import pyttsx as pys
import engineio
import datetime
import wikipedia
import os
import webbrowser
from utils import *
from movie import *
from youtube import *

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

greet()

#bot starts taking commands
c = 0 
while True:
    print("Start")
    p = "i am man"
    print(p.find("am"))
    inst = Command()
    def main(query):
        if query!= None :
            instruction = query
        else :
            instruction = Command()
 
        if "wikipedia" in instruction.lower():
            speak("Searching Wikipedia..")
            inst = instruction.replace("wikipedia","")
            results = wikipedia.summary(inst,sentences=2)
            print(results)
            speak(results)
            main(None)

        if "open youtube" in instruction.lower():
            speak("Opening youtube")
            bot = Youtube()
            query = bot.play()
            main(query)
            # speak("Opening youtube")
            # webbrowser.open("www.youtube.com")
            # speak("what would you like to see on youtube?")
            # search = Command()

        if "movie review" in instruction.lower():
            speak("what is the name of the movie?")
            review = Command()
            bot = Movie()
            rating = bot.movie_review(review)
            if rating != None:
                speak("The IMDB rating of this movie is" + rating)
            else:
                speak("The IMDB rating for this movie is not available")
            

        elif "close" in instruction:
            speak("Pleasure talking to you.....Byeeee....Have a nice day!!")
            exit()

        # elif "open youtube" or "wikipedia" or  "close" or "movie review" not in instruction:
        #     speak("I could not get an instruction to perform")
    
    if(c>0):
        speak("What should I do next?")

    main(inst)
    c = c + 1




