import sqlite3
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)
from webdriver_manager.chrome import ChromeDriverManager

def insert_lab(title, created_at, image_url, image_description, all_description):
    conn = sqlite3.connect("ai_posts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            created_at TEXT,
            image_url TEXT,
            image_description TEXT,
            all_description TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO posts (title, created_at, image_url, image_description, all_description)
        VALUES (?, ?, ?, ?, ?)
    """, (title, created_at, image_url, image_description, all_description))
    conn.commit()
    conn.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://shaxzodbek.com/")
driver.maximize_window()
sleep(4)

#Post bo'limiga o'tadi
try:
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/nav/ul/li[2]/a"))
    )
    btn.click()
    sleep(2)
except TimeoutException:
    print("Post bo‘limiga o‘tish uchun element topilmayapti!")
    driver.quit()
    exit()

#Next tugmasini bosadi
for i in range(2):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        sleep(1)
        try:
            next_button.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", next_button)
        sleep(2)
        print(f"{i+1}-marta 'Next' tugmasi bosildi.")
    except TimeoutException:
        print(f"Next tugmasi topilmadi ({i+1}-marta bosishda), lekin davom etamiz.")

#Malumotlarni chiqaradi
try:
    read_more_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//h4/a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'the rise of ai in everyday life')]/ancestor::article//a[@class='read-more']"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", read_more_btn)
    sleep(1)
    try:
        read_more_btn.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", read_more_btn)
    sleep(3)
except TimeoutException:
    print("Maqola topilmadi!")
    driver.quit()
    exit()

try:
    #Sarlavha qismi
    title = driver.find_element(By.XPATH, "//h1[contains(text(), 'The Rise of AI in Everyday Life')]").text
    print("Sarlavha:", title)

    #Sanani chiqarib beradi
    try:
        date_elem = driver.find_element(By.XPATH, "//div[@class='article-date']")
        raw_date = date_elem.text.strip()
        date_obj = datetime.strptime(raw_date, "%B %d, %Y")
        created_at = date_obj.strftime("%Y-%m-%d")  # To‘liq sana
        print("Yaratilgan sana:", created_at)
    except Exception:
        created_at = "Noma'lum"
        print("Sana topilmadi yoki format noto‘g‘ri.")

    #Rasm URL olib beradi
    try:
        image_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='The Rise of AI in Everyday Life']"))
        )
        src = image_elem.get_attribute("src")
        if src.startswith("/"):
            image_url = "https://shaxzodbek.com" + src
        else:
            image_url = src
        print("Rasm URL:", image_url)
    except TimeoutException:
        image_url = "Yo'q"
        print("Rasm topilmadi.")

    #Matn rasm tasvirini chiqaradi
    try:
        content_section = driver.find_element(By.XPATH, "//div[contains(@class,'content-section')]")
        image_description = content_section.text.strip()
        all_description = content_section.get_attribute("innerHTML").strip()
        print("Rasm tasviri:", image_description)
    except NoSuchElementException:
        image_description = ""
        all_description = ""
        print("Matn topilmadi.")

    insert_lab(title, created_at, image_url, image_description, all_description)
    print("Bazaga yozildi.")

except NoSuchElementException as e:
    print(f"Element topilmadi: {e}")

driver.quit()
