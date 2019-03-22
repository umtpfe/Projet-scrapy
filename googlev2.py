from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://www.google.com"
driver.get(url)

search = driver.find_element_by_name("q")
search.send_keys("chanel")

searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')

searchbutton.click()

while True:

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