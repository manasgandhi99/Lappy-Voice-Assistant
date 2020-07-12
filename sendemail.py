import smtplib

class sendEmail():
    def sendEmail(self,to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('manasgandhi01@gmail.com','manadu17#')
        server.sendmail("manasgandhi01@gmail.com", to, content)
        server.close()
