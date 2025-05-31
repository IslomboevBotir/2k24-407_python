from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    service = Service()  # chromedriver PATH tizimga qo'shilgan deb hisoblaymiz
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--incognito")
    # options.add_argument("--headless")  # agar fon rejimida ishga tushirmoqchi bo'lsangiz
    return webdriver.Chrome(service=service, options=options)
