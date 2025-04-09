from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

wait = WebDriverWait(driver, 30)
driver.get("https://como-tower.ae/")
pop_up = ("xpath", "//*[@id='time-popup']/div/div")
wait.until(EC.invisibility_of_element_located(pop_up))

print(driver.title)

driver.quit()
