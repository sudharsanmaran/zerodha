from selenium import webdriver

browser = webdriver.Chrome()
service = webdriver.chrome.service.Service('./chromedriver')
service.start()