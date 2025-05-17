from time import sleep

def wait(seconds=2):
    sleep(seconds)

def scroll_to(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(1)

def scroll_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
