from selenium import webdriver
import time

PROXY = "193.70.41.31:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--ignore_certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(2)
chrome.close()
