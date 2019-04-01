from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import threading

driver = webdriver.Firefox()
url = "http://www.google.com/search?q=chanel"


while True:

    
    driver.get(url)

    val = True

    while val:
        try:
            results = driver.find_elements_by_xpath('//*[@id="rso"]')

            for result in results:
                print(result.text)
       
            nextbutton = driver.find_element_by_xpath('//*[@id="pnnext"]')  # si le bouton next n existe pas il va dans l'exception
            nextbutton.click()

        except :

            try:
               
                frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
               
                driver.switch_to.frame(frame)
                
                driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
                
                time.sleep(120)
                driver.switch_to.default_content()
                
                
                continue

            except:

                
            
                val = False

