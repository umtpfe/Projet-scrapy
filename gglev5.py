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

                profile = webdriver.FirefoxProfile()

                driver = webdriver.Firefox(firefox_profile=profile)

               
                driver.get("https://www.sslproxies.org/")

                tbody = driver.find_element_by_tag_name("tbody")

                cell = tbody.find_elements_by_tag_name("tr")

                for column in cell:
                    column = column.text.split(" ")
                    host = column[0]
                    port = column[1]
                    profile.set_preference("network.proxy.type", 1)
                    profile.set_preference("network.proxy.http", host)
                    profile.set_preference("network.proxy.http_port", int(port) )
                    profile.set_preference("network.proxy.ssl", host)
                    profile.set_preference("network.proxy.ssl_port", int(port) )
                 
                driver.quit()
                driver = webdriver.Firefox(firefox_profile=profile)



                time.sleep(30)
                driver.switch_to.default_content()
                
                
                continue

            except:

                
            
                val = False

