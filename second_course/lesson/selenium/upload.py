# import time
# import os

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# seleniu_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=seleniu_options)
# driver.get("https://www.ilovepdf.com/word_to_pdf")

# upload_file = driver.find_element("xpath", "//input[@type='file']")
# time.sleep(2)
# upload_file.send_keys(f"{os.getcwd()}/resources/Muxtorov_Shaxzodbek_cv.docx")
# time.sleep(10)

import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

selenium_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=selenium_options)
driver.get("https://www.ilovepdf.com/word_to_pdf")

upload_file = driver.find_element("xpath", "//input[@type='file']")
time.sleep(2)
upload_file.send_keys(f"{os.getcwd()}/resources/Muxtorov_Shaxzodbek_cv.docx")
time.sleep(5)

default_download_path = {
    "download.default_directory": f"{os.getcwd()}/resources",
}

selenium_options.add_experimental_option("prefs", default_download_path)
buttonslist = driver.find_elements(By.ID, "processTask")[0].click()
time.sleep(15)