from selenium import webdriver
import time
import requests 
import threading  

proxy = "125.27.251.41:51480" # IP:PORT or HOST:PORT

def poxy_request(request_type, url):
	while 1:
		try:
			proxy = get_proxy()
			print("using proxy: ".format(proxy))
			r = resquests.resquest(resquest_type, url, proxies=proxy)
			break
		except:
			pass	

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)
chrome_options.add_argument('--ignore_certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.pagesjaunes.fr/annuaire/paris-75/avocat-droit-du-travail"

driver.get(url)

contacts = driver.find_elements_by_class_name("barre-liens-contact ")

for contact in contacts:
	print(contact[0].text + ","+ "\n" )

time.sleep(5)
driver.close()
print("fin")


