import csv
from selenium import webdriver

MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5

with open ("listemail.csv", "w") as f :
  f.write("emails \n")


driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  url = "http://jecherchemonexpertcomptable.oecmaroc.com/users/index/" + page_num +" "
    
  driver.get(url)

  emails = driver.find_elements_by_xpath('//*[@id="page-content"]')

  
  num_page_items = len(emails)
  with open("listemail.csv", "w") as f:
    for i in range(num_page_items):
      f.write(emails[i].text + "," + "\n")
      
      


driver.close()
print("fin")


