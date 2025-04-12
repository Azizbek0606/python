import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import *

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
wait = WebDriverWait(driver, 30)

driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")

popup_xpath = '//*[@class="popup-modal__body modal-body"]/div'
wait.until(EC.visibility_of_element_located((By.XPATH, popup_xpath)))

name_input = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@class="popup-modal__body modal-body"]/div/form/div[1]/input',
        )
    )
)
name_input.send_keys(generate_name())

email_input = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@class="popup-modal__body modal-body"]/div/form/div[2]/input',
        )
    )
)
email_input.send_keys(generate_email())

phone_number_input = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@class="popup-modal__body modal-body"]/div/form/div[3]/div/input',
        )
    )
)
phone_number_input.send_keys(generate_phone_number())

time.sleep(1)

btn_to_submit = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="popup-modal__btn btn btn-gradient"]')
    )
)
btn_to_submit.click()

time.sleep(1)

success_modal = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="swal2-confirm swal2-styled"]')
    )
)
success_modal.click()

time.sleep(1)

close_form_modal = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="popup-modal__close-btn btn"]')
    )
)
close_form_modal.click()

time.sleep(1)

second_form = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@class='about-brochure__form download-brochure-form gs-anim']")
    )
)


driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", second_form
)
time.sleep(1)
# download-brochure-form__form
# download-brochure-form__input