from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from utils import *
from sendtext import *

class Whatsapp:
    
    def __init__(self,to,content):
        # self.driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.to = to
        self.content = content

    def msg(self):
        self.driver.get(url="https://web.whatsapp.com")
        # search = self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        # search.click()
        speak("Please scan the QR code for Whatsapp Web to operate.")
        time.sleep(15)
        inst = sendText(self,self.to,self.content)
        return inst
        

# bot = Whatsapp
# man = bot("You","Thanks").msg()
# print(man)