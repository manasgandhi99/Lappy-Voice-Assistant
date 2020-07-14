import smtplib

class sendEmail:
    def send(self,to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('email@gmail.com','###')
        server.sendmail("example@gmail.com", to, content)
        server.close()
