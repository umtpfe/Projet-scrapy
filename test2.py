import os
import csv
import re
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "200.37.54.10")
profile.set_preference("network.proxy.http_port", 57040)
profile.update_preferences()

MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5


driver = webdriver.Firefox(firefox_profile=profile)

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  url = "http://jecherchemonexpertcomptable.oecmaroc.com/users/index/" + page_num +" "
    
  driver.get(url)

  ids = driver.find_elements_by_xpath('//*[@id="page-content"]')

  
  num_page_items = len(ids)
  with f.open("idmail.csv", "w") as f:
    for i in range(num_page_items):
      f.write(ids[i].text + "," + "\n")
      time.sleep(1)
      f.close()
      
      
  driver.close()
  print("fin")