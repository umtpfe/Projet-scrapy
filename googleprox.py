from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
from threading import Thread
import sys
import random

#profile = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(firefox_profile=profile)


dicoProxy = {}
def recupDico():
    i=0
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=profile)               
    driver.get("https://www.sslproxies.org/")
    tbody = driver.find_element_by_tag_name("tbody")
    cell = tbody.find_elements_by_tag_name("tr")
    for column in cell:
        column = column.text.split(" ")
        host = column[0]
        port = column[1]
        dicoProxy[i] = host+":"+port
        i+=1
    driver.quit()




        
def proxyChange(valeur):
    print("Appel de la fonction")
    monroxy = dicoProxy[valeur].split(':')
    return monroxy


   
i=0
recupDico()
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)
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
                driver.switch_to.default_content()
                time.sleep(10)
                driver.switch_to.default_content()
                try:
                    print ("t1")
                    
                  
                    ProxyHost = "185.132.178.210"
                    ProxyPort = "1080"



                    def ChangeProxy(ProxyHost , ProxyPort):

                        pp = proxyChange(i)


                        profile = webdriver.FirefoxProfile() 
                        profile.set_preference("network.proxy.type", 1)
                        profile.set_preference("network.proxy.http", pp[0] )
                        profile.set_preference("network.proxy.http_port", int(pp[1]))
                        profile.set_preference("network.proxy.ssl", pp[0])
                        profile.set_preference("network.proxy.ssl_port",  int(pp[1]))
                        profile.set_preference("general.useragent.override","whater_useragent")
                        profile.set_preference("network.proxy.socks_version", 5)
                        profile.update_preferences()
                        return webdriver.Firefox(firefox_profile=profile) 

                    def FixProxy():
                        profile = webdriver.Firefox()
                        profile.set_preference("network.proxy.type", 0)
                        return webdriver.Firefox(firefox_profile=profile)

                    driver = ChangeProxy(ProxyHost ,ProxyPort)
                    time.sleep(20)
                    i+=1
                    
                except:
                    print("timeout")

                    wait = WebDriverWait(driver, 30);
                    try:
                        result = wait.until(EC.element_to_be_located((By.XPATH, '//*[@id="rso"]')))
                    except TimeoutException:
                        driver.refresh()                             
                
                
                #continue

            except:       
            
                val = False