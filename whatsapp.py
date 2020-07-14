from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils import *
import time

class Whatsapp():
    
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def msg(self,to,content):
        self.driver.get(url="https://web.whatsapp.com")
        # search = self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        # search.click()
        speak("Please scan the QR code for Whatsapp Web to operate.")
        time.sleep(15)
        inst = sendText(to,content)
        return inst.lower()

    
    def sendText(self,to,content):
        elem = self.driver.find_element(By.XPATH,"//*[@id='side']/div[1]/div/label/div/div[2]")
        print("Element is visible? " + str(elem.is_displayed()))
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        elem.send_keys(to)
        elem.send_keys(Keys.ENTER)
        while True:
            sea = self.driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            sea.click()
            sea.send_keys(content)
            sea.send_keys(Keys.ENTER)
            speak("Would you like to message the same person further?")
            inst = Command()
            if inst != "Yes":
                return inst.lower()
            elif inst == "other person":
                speak("Whom would you like to text?")
                audio = Command()
                speak("What is the message?")
                text = Command()
                sendText(audio,text)
       
        
        print("Done")

    
   
       

bot = Whatsapp()
bot.msg("You","Ghost Rider")