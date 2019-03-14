from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time 
import threading
import multiprocessing

PROXY = "195.94.243.206:47054" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--ignore_certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

MAX_PAGE_NUM = 16
MAX_PAGE_DIG = 3

with open ("contacts2.csv", "w") as f :



	driver = webdriver.Chrome(options=chrome_options)
	
for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=avocat%20droit%20du%20travail&ou=paris-75&proximite=0&quoiQuiInterprete=avocat%20droit%20du%20travail&contexte=V0RcB2CgpYFodNUZBe%2BLCQ%3D%3D&idOu=L07505600&page=" + page_num +" "

driver.get(url)

try:
  	WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="bi-contact-06785617000002C0001"]/ul[1]')))

		
except TimeoutException:
  		print('chargement de la page')

contacts = driver.find_elements_by_xpath('//*[@id="bi-contact-06253114000031C0001"]')


num_page_items = len(contacts)
for i in range(num_page_items):
      f.write(contacts2[i].text + "," + "\n")
      print('contacts2: ')
      print(contacts2)
      f.close()

    	

driver.close()

print("fin")


