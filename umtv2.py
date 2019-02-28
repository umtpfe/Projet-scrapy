from selenium import webdriver
import csv 

MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5

chrome_path = r"C:\Users\Issa Sangare\Desktop\exemples python\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)

url = ("http://jecherchemonexpertcomptable.oecmaroc.com/users/index/" + page_num +" ")

driver.get(url)


emails = driver.find_elements_by_xpath('//*[@id="page-content"]')

num_page_items = len(emails)
with open ("email.csv", "w") as f:
	for i in range(num_page_items):
		f.write("emails \n")
		f.close()

for email in emails:
	print(email)

driver.close()
print("Fin du programme")