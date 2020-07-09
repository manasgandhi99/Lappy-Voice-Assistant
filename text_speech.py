import pyttsx as pys
import engineio
engineio = pys.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 160)    
engineio.setProperty('voice',voices[1].id)
volume = engineio.getProperty('volume')   
engineio.setProperty('volume',1.0)
engineio.say("Heyyyyyy , waddup waddup??")
engineio.runAndWait()
engineio.stop()





# print("Hii")  
