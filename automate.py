import speech_recognition as sr
import pyttsx as pys
import engineio

r = sr.Recognizer()

#bot says opening words
engineio = pys.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 150)    
engineio.setProperty('voice',voices[1].id)
volume = engineio.getProperty('volume') 
engineio.setProperty('volume',1.0)
engineio.say("Heyyyyyy , waddup waddup??")
engineio.runAndWait()

with sr.Microphone() as source:
    text = r.listen(source)
    
    try:
        instruction = r.recognize_google(text)
        print(instruction)
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError as e:
        print(e)

#getting info from wiki


