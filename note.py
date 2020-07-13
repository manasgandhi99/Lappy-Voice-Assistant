import datetime
import subprocess

class Notepad():

    def note(self,text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":","-") + "-note.txt"
        with open(file_name,"w") as f:
            f.write(text)
        
        notepad = "notepad.exe"
        subprocess.Popen([notepad,file_name])

# note("Hi i am good")