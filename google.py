import selenium.webdriver as webdriver

def get_results(search_term):
    url = "https://www.google.com/"
    browser = webdriver.Chrome()
    browser.get(url)
    search_box = browser.find_element_by_name("q")
    search_box.send_keys(search_term)
    search_box.submit()
    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
        links = browser.find_elements_by_xpath("//h3//a")
    results = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
        browser.close()
        return results

response = get_results("Chanel")