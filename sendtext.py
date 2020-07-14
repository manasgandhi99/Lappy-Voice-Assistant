from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils import *

def sendText(self,to,content):
    elem = self.driver.find_element(By.XPATH,"//*[@id='side']/div[1]/div/label/div/div[2]")
    print("Element is visible? " + str(elem.is_displayed()))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    elem.send_keys(to)
    elem.send_keys(Keys.ENTER)

    # while True:
    sea = self.driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    sea.click()
    sea.send_keys(content)
    sea.send_keys(Keys.ENTER)

    speak("Would you like to message the same person further?")
    inst = Command()

    if inst == "other person":
        speak("Whom would you like to text?")
        rec = Command()
        speak("What is the message?")
        text = Command()
        sendText(self,rec,text)
    elif inst == "yes":
        speak("What should I send?")
        text = Command()                
        sendText(self,self.to,text)
    elif inst != "yes":
        return inst
    
    print("Done")