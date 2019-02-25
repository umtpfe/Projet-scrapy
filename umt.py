import csv
from selenium import webdriver

MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5

with open ("liste mail.csv", "w") as f :
  f.write("")

#chrome_path = r"C:\Users\Issa Sangare\Desktop\exemples python\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  url = "http://jecherchemonexpertcomptable.oecmaroc.com/users/index/" + page_num +" "
    
  driver.get(url)

  emails = driver.find_elements_by_xpath('//*[@id="antique-all"]/div[2]/div[1]/div/h4/a')
  
  num_page_items = len(emails)
  with open("liste mail.csv", "a") as f:
    for i in range(num_page_items):
      f.write(r'[\w\.-]+@[\w\.-]+', doc)
      #f.write(emails[i],text + "," + "\n")


driver.close()
#driver.get("http://jecherchemonexpertcomptable.oecmaroc.com/users/index/page:01")

#doc = driver.page_source

#emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

#for email in emails:
# print(email)

#driver.close()
#print("Fin du programme")