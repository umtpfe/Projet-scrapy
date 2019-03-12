import csv
from selenium import webdriver
import time

PROXY = "5.58.85.32:43214" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--ignore_certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

MAX_PAGE_NUM = 16
MAX_PAGE_DIG = 3

with open ("contacts.csv", "w") as f :
  


	driver = webdriver.Chrome(options=chrome_options)

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  url = "https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=avocat%20droit%20du%20travail&ou=paris-75&proximite=0&quoiQuiInterprete=avocat%20droit%20du%20travail&contexte=V0RcB2CgpYFodNUZBe%2BLCQ%3D%3D&idOu=L07505600&page=" + page_num +" "
    
  driver.get(url)
  time.sleep(10)
  contacts = driver.find_elements_by_xpath('//*[@id="bi-contact-06253114000031C0001"]')

  
  num_page_items = len(contacts)
for i in range(num_page_items):
      f.write(contacts[i].text + "," + "\n")
            
      driver.close()
print("fin")
