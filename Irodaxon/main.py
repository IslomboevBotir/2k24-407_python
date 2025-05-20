import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from db import get_connection, create_certification_table

# Logging sozlamalari
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def save_certification_to_db(data):
    """Ma'lumotlarni SQLite bazasiga saqlash."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO certifications (header, date, image, description)
        VALUES (?, ?, ?, ?)
    """, (data["header"], data["date"], data["image"], data["description"]))
    conn.commit()
    cur.close()
    conn.close()
    logging.info("✅ Ma'lumotlar SQLite bazaga saqlandi.")


def start_browser():
    """Brauzerni ishga tushurish."""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def wait_for_element(driver, by, value, timeout=10):
    """Elementni kutish uchun qulay funksiya."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        logging.warning(f"⛔ Element topilmadi: {value}")
        return None


def scrape_pdp_certification(driver):
    """PDP certification sahifasidan ma'lumotlarni ajratib olish."""
    driver.get("https://shaxzodbek.com/")

    try:
        certifications_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Certifications"))
        )
        certifications_link.click()
    except TimeoutException:
        logging.error("❌ 'Certifications' havolasi topilmadi.")
        return None

    while True:
        time.sleep(2)
        cards = driver.find_elements(By.CLASS_NAME, "certification-content")
        for card in cards:
            if "PDP Academy" in card.text:
                logging.info("🎯 PDP Academy topildi.")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)
                try:
                    card.find_element(By.PARTIAL_LINK_TEXT, "PDP").click()
                except NoSuchElementException:
                    logging.warning("⚠️ PDP havolasi bosilmadi.")
                    continue

                time.sleep(2)
                data = {
                    "header": wait_for_element(driver, By.XPATH, "//main/section/div/header/h3").text,
                    "date": wait_for_element(driver, By.XPATH, "//main/section/div/header/div/div").text,
                    "image": wait_for_element(driver, By.XPATH, "//main/section/div/div[1]/div[1]/img").get_attribute("src"),
                    "description": wait_for_element(driver, By.XPATH, "//main/section/div/div[1]/div[2]").text,
                }
                return data

        # Next tugmasi orqali sahifalanish
        try:
            next_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
            next_btn.click()
        except TimeoutException:
            logging.info("🔍 PDP Academy topilmadi. Boshqa sahifa yo‘q.")
            break

    return None


def main():
    """Asosiy ishga tushirish funksiyasi."""
    create_certification_table()
    driver = start_browser()

    try:
        data = scrape_pdp_certification(driver)
        if data:
            save_certification_to_db(data)
        else:
            logging.warning("⚠️ Ma'lumot topilmadi.")
    except Exception as e:
        logging.exception("❗ Xatolik yuz berdi:")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
