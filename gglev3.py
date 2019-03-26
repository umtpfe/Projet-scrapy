from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

driver = webdriver.Firefox()
url = "http://www.google.com"
driver.get(url)

search = driver.find_element_by_name("q")
search.send_keys("chanel")

searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')

searchbutton.click()

while True:
    try:
        results = driver.find_elements_by_xpath('//*[@id="rso"]')
       
        for result in results:
            print(result.text)
       
        urls = []
       
        for result in results:
            urls.append(result.get_attribute("href"))
       
        for url in urls: 
            print(url)
       
        nextbutton = driver.find_element_by_xpath('//*[@id="pnnext"]')
        nextbutton.click()

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pnnext"]')))
        time.sleep(10)

             
    
    except NoSuchElementException:
        
        wait = WebDriverWait(driver, 10)

        element = wait.until(EC.visibility_of_element_clickable((By.XPATH, '//*[@id="pnnext"]')))
        element.click()
        time.sleep(10)