from selenium.webdriver.support.ui import WebDriverWait

def wait_to(driver, element):
    return WebDriverWait(driver, 20).until(element)  # Kutish vaqtini 20 soniyaga oshirib qo‘ydim