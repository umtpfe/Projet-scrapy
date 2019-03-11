from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type",1)
profile.set_preference("network.proxy.http","193.70.41.31")
profile.set_preference("network.proxy.http_port", 8080)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)
driver.get("http://whatismyipaddress.com")
time.sleep(2)
driver.close()