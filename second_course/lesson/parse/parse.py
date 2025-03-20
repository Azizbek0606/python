from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/login/ru")
print(driver.title)
assert driver.current_url == "https://www.linkedin.com/login/ru"
print(driver.current_url)
