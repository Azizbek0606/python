import pytest
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False, 
        slow_mo=200,
        args=["--start-maximized"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.set_default_navigation_timeout(20000)
    page.set_default_timeout(20000)

    page.goto("https://kassa-dev.smartpos.uz")

    if "Smartpos Web-Kassa" in page.title():
        page.locator("#username").fill("905439771")
        page.locator("#password").fill("832145")
        page.locator("#remember").check()
        time.sleep(1)
        page.locator("remember").uncheck()
        time.sleep(3)
        page.locator("//*[@id'Войти']")

    time.sleep(5)
    browser.close()
