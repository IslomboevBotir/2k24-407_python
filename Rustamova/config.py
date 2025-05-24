from selenium import webdriver
DB_HOST = "localhost"
DB_NAME = "selenium"
DB_USER = "mahliyo"
DB_PASSWORD = "mahliyo"



def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--incognito")
    return webdriver.Chrome(options=options)
