import speech_recognition as sr
import pyttsx as pys
import engineio
import datetime
import wikipedia
import os
import webbrowser

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
            speak("Err..There was some error please try again!")
            return None
        except sr.RequestError as e:
            print(e)
            return None