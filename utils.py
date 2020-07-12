import speech_recognition as sr
import pyttsx as pys
import engineio
import datetime
import wikipedia
import os
import webbrowser
import playsound
from gtts import gTTS

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

#this func can save an audio
def saveVoice(audio):
    tts = gTTS(text= audio,Lang="en")
    filename = "voice.mp3"
    tts.save()
    playsound.playsound(filename)

#bot will take the specific command
def Command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        
        try:
            instruction = r.recognize_google(audio)
            print(instruction)
        except sr.UnknownValueError:
            print("Error")
            speak("Oopss..There was some error please try again!")
            # return None
        except sr.RequestError as e:
            print(e)
            speak("OOpss..There was some error please try again!")
            # return None
    return instruction.lower()
