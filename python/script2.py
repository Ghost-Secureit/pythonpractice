from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"/usr/bin/firefox"
driver = webdriver.Firefox(options=options, service=None)

driver.get('https://www.google.com')