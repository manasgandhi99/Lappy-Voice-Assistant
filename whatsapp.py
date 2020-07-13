from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyttsx as pys

class Whatsapp():
    
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def msg(self,to,name):
        self.driver.get(url="https://web.whatsapp.com")
        # search = self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        # search.click()
        meci = self.driver.find_elements_by_class_name('_2kHpK')
        print("meci hua")
        for items in meci:
            print("Hi")
            scor = items.find_element_by_class_name('_3ko75 _5h6Y_ _3Whw5')
            print (scor.text)    
            if scor.text == to :
                input=self.driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div[2]")
                input.click()
                print("Hello")
                input.send_keys(name)
                input.send_keys(Keys.ENTER)
                break
                # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]"))).click()
        # element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
        # driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.CSS_SELECTOR, "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")))
        # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='loadingWhiteBox']"))))
        # rating = self.driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/a[2]/span[1]")
        #    String text = self.driver.findElement(By.tagName("span")).getText();
        # try:
        #     elems = self.driver.find_elements_by_xpath("//*[@id='rso']/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/a/span[1]")[1].text
        #     print(elems)
        #     return elems
        # except Exception as e:
        #     print("Error")
        #     return None
        
        print("Done")
        # if elems:
        #     return elems
        # else:
        #     return None

bot = Whatsapp()
bot.msg("You","Ghost Rider")