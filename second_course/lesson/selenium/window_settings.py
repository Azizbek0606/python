# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# option = webdriver.ChromeOptions()
# option.add_argument("--headless")
# option.add_argument("--window-size=1920,1080")
# option.add_argument("--incognito")
# option.add_argument("--ignore-certificate-errors")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=option)

# driver.get("https://axcapital.ae")
# print(driver.title)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://axcapital.ae")

elements = driver.find_elements(By.CLASS_NAME, "content_link")

for index, element in enumerate(elements):
    print(f"{index+1}. {element.text}")

driver.quit()
