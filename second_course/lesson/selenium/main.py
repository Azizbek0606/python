import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.axcapital.ae/")

l = driver.find_element("xpath", "//input[@placeholder='Your name']")
driver.execute_script("arguments[0].scrollIntoView()", l)

time.sleep(5)

l.click()
l.send_keys("Lorem Ipsum")

time.sleep(10)
