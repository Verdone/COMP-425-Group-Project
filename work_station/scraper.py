import selenium
from selenium import webdriver



options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://platesmania.com/ca/gallery-2")

driver.quit()
