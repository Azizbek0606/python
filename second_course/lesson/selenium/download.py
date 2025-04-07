import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

selenium_options = webdriver.ChromeOptions()
default_download_path = {
    "download.default_directory": f"{os.getcwd()}/download",
}

selenium_options.add_experimental_option("prefs", default_download_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://shaxzodbek.com/")
time.sleep(2)
driver.find_elements("xpath", "//a")[10].click()
time.sleep(2)
