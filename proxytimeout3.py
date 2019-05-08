from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import threading
import sys
import random



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
    print("Fonction de recuperation de Proxy")
    monroxy = dicoProxy[valeur].split(':')
    return monroxy



def ChangeProxy():

    pp = proxyChange(i)
    print("Changement de proxy")
    profile = webdriver.FirefoxProfile() 
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.https", pp[0] )
    profile.set_preference("network.proxy.https_port", int(pp[1]))
    profile.set_preference("network.proxy.ssl", pp[0]) 
    profile.set_preference("network.proxy.ssl_port",  int(pp[1]))
    profile.set_preference("general.useragent.override", "whater_useragent")
    profile.set_preference("network.proxy.socks_version", 5)
    profile.update_preferences()
    print("Proxy changé")
    return webdriver.Firefox(firefox_profile=profile) 

def FixProxy():
    profile = webdriver.Firefox()
    profile.set_preference("network.proxy.type", 0)
    return webdriver.Firefox(firefox_profile=profile)

dicoProxy = {}   
i=0
recupDico()  
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)

while True:
    url = "http://www.google.com/search?q=chanel"

    driver.get(url)
    while True:
        # Chercher elements
        results = driver.find_elements_by_xpath('//*[@id="rso"]')

        for result in results:
            print(result.text)

        try:
            # clicker next
            nextbutton = driver.find_element_by_xpath('//*[@id="pnnext"]')  # si le bouton next n existe pas il va dans l'exception
            nextbutton.click()

        except:
            # Plus de Button next
            print("captcha ?")
            try:
                # captcha 
                frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')

                driver.switch_to.frame(frame)
                driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
                driver.switch_to.default_content()
                time.sleep(10)
                driver.switch_to.default_content()
                th1 = threading.Thread(target = ChangeProxy)
                th1.start()
                th1.join()
                driver = webdriver.Firefox(firefox_profile=profile)
                i+=1

            except TimeoutException: 
                # ce n'est pas un captcha
                print("timeout ?")
                th1 = threading.Thread(target = ChangeProxy)
                th1.start()
                th1.join()
                driver = ChangeProxy()
                i+=1
                break

            except:
                print("last page")
                break