from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import threading
import sys
import random


dicoProxy = {}
def recupDico():
    dicoProxy[0] = "34.244.2.233:8123"
    dicoProxy[1] = "85.93.47.137:8080"
    dicoProxy[2] = "46.63.162.171:8080"
    dicoProxy[3] = "138.197.180.57:3128"
    dicoProxy[4] = "85.30.219.120:46761"
    dicoProxy[5] = "85.15.189.121:41033"
    dicoProxy[6] = "103.57.21.30:53281"
    dicoProxy[7] = "103.76.188.209:34424"
    dicoProxy[8] = "103.89.253.246:3128"
    dicoProxy[9] = "105.30.17.3:53281"

        
def proxyChange(valeur):
    print("Fonction de recuperation de Proxy")
    monroxy = dicoProxy[valeur].split(':')
    return monroxy

   
i=0
recupDico()

def ChangeProxy():

    pp = proxyChange(i)
    print("Changement de proxy")


    profile = webdriver.FirefoxProfile() 
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.https", pp[0] )
    profile.set_preference("network.proxy.https_port", int(pp[1]))
    profile.set_preference("network.proxy.ssl", pp[0])
    profile.set_preference("network.proxy.ssl_port",  int(pp[1]))
    profile.set_preference("general.useragent.override","whater_useragent")
    profile.set_preference("network.proxy.socks_version", 5)
    profile.update_preferences()

    print("Proxy changé")
    return webdriver.Firefox(firefox_profile=profile) 

def FixProxy():
    profile = webdriver.Firefox()
    profile.set_preference("network.proxy.type", 0)
    return webdriver.Firefox(firefox_profile=profile)
  
  

profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)
url = "http://www.google.com/search?q=chanel+ext:pdf"
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
        print("lastpage")
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
            driver = ChangeProxy()
            time.sleep(10)
            i+=1

        except: 
            # ce n'est pas un captcha
            break