from selenium import webdriver
import re

chrome_path = r"C:\Users\Issa Sangare\Desktop\exemples python\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://aapa.ca/fr/contact.php')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
	print(email)