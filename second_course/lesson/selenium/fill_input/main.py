import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import (
    generate_name,
    generate_email,
    generate_phone_number,
)  # utils fayldan import

# Skrinshotlarni saqlash uchun papka yaratish
SCREENSHOT_DIR = "screenshots"
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

# Chrome driver sozlamalari
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Driverni ishga tushirish
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
wait = WebDriverWait(driver, 30)

# Saytga kirish
driver.get("https://sales-inquiries.ae/axcapital/al-jazi/")


def fill_form(form_element, form_index):
    """Berilgan formani to'ldiradi va skrinshot oladi"""
    try:
        # Forma inputlarini topish
        name_input = form_element.find_elements(
            By.XPATH, ".//input[@placeholder='Name' or contains(@placeholder, 'name')]"
        )
        email_input = form_element.find_elements(
            By.XPATH,
            ".//input[@placeholder='Email' or contains(@placeholder, 'email')]",
        )
        phone_input = form_element.find_elements(
            By.XPATH,
            ".//input[@placeholder='Phone' or contains(@placeholder, 'phone')]",
        )

        # Inputlarni to'ldirish
        if name_input:
            name_input[0].send_keys(generate_name())
        if email_input:
            email_input[0].send_keys(generate_email())
        if phone_input:
            phone_input[0].send_keys(generate_phone_number())

        time.sleep(1)

        # Submit tugmasini topish va bosish
        submit_button = form_element.find_elements(
            By.XPATH, ".//button[contains(@class, 'btn') or @type='submit']"
        )
        if submit_button:
            driver.execute_script("arguments[0].click();", submit_button[0])
            time.sleep(2)

            # Muvaffaqiyat modalini tekshirish va yopish
            try:
                success_modal = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//button[contains(@class, 'swal2-confirm') or contains(@class, 'confirm')]",
                        )
                    )
                )
                success_modal.click()
                time.sleep(1)
            except:
                pass

            # Forma modalini yopish
            try:
                close_button = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//button[contains(@class, 'close') or contains(@class, 'popup-modal__close')]",
                        )
                    )
                )
                close_button.click()
                time.sleep(1)
            except:
                pass

        # Skrinshot olish
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            form_element,
        )
        time.sleep(1)
        screenshot_path = os.path.join(
            SCREENSHOT_DIR, f"form_{form_index}_screenshot.png"
        )
        driver.save_screenshot(screenshot_path)
        print(f"Skrinshot saqlandi: {screenshot_path}")

    except Exception as e:
        print(f"Forma {form_index} ni to'ldirishda xato: {str(e)}")


# Barcha formalarni topish va to'ldirish
try:
    # Popup formalarini topish
    forms = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//form | //div[contains(@class, 'form')]")
        )
    )

    print(f"Topilgan formalar soni: {len(forms)}")

    # Har bir formani to'ldirish
    for index, form in enumerate(forms, 1):
        try:
            # Forma ko'rinadigan joyga scroll qilish
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                form,
            )
            time.sleep(1)

            # Forma ko'rinadimi tekshirish
            if form.is_displayed():
                print(f"Forma {index} ni to'ldirish...")
                fill_form(form, index)
            else:
                print(f"Forma {index} ko'rinmayapti, o'tkazib yuborildi")

        except Exception as e:
            print(f"Forma {index} bilan ishlashda xato: {str(e)}")
            continue

except Exception as e:
    print(f"Formlarni topishda xato: {str(e)}")

finally:
    # Brauzerni yopish
    time.sleep(2)
    driver.quit()
