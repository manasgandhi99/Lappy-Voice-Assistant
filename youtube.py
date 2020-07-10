from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyttsx as pys
from utils import *

class Youtube():
    
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def play(self):
        self.driver.get(url="https://www.youtube.com")
        # search = self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        # search.click() 
        # webbrowser.open("www.youtube.com")
        c = 0
        speak("what would you like me to do on youtube?")
        while True:
            search = Command()
            # c = c + 1
            list1 = ["search for","search","look for" ,"find"]
            for word in list1:
                if word in search:
                    speak("Searching..")
                    # elem=self.driver.find_element(By.XPATH,"//*[@id='search']")
                    elem = self.driver.find_element(By.XPATH,"//input[@id='search']")
                    elem.clear()
                    print("Element is visible? " + str(elem.is_displayed()))
                    self.driver.implicitly_wait(10)
                    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
                    # WebDriverWait(self.driver,40).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']"))).click().send_keys(search)
                    # elem.click()
                    print(word)
                    
                    elem.send_keys(search)
                    elem.send_keys(Keys.ENTER)
                    print("hiiiii")
                    c = c + 1
                    print(c)
                    break
                    # return 1
                    # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search-icon-legacy']"))).click()
            
            list2 = ["watch","see","chill","play"]
            for word in list2:
                if word in search:
                    speak("Searching..")
                    self.driver.get(url="https://www.youtube.com/results?search_query="+search)
                    # elem=self.driver.find_element(By.XPATH,"//input[@id='search']")
                    # elem.click()
                    # elem.send_keys(search)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dismissable']/div"))).click()
                    # return 1
                    c = c + 1
                    print(c)
                    break

            if c == 0:
                print("nooo")
                speak("Okay, Thats alright!")
                return search
            
            print("Done")
            c = 0

# bot = Youtube()
# bot.play()