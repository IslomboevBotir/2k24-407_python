# main.py

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from database import get_connection, create_table_if_not_exists

load_dotenv()

BASE_URL = os.getenv("BASE_URL") or "https://shaxzodbek.com/"
TARGET_SLUG = os.getenv("TARGET_SLUG") or "ai-powered-chatbot/"
SCREENSHOT_NAME = os.getenv("SCREENSHOT_NAME") or "ai_powered_chatbot.png"

def init_driver():
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except WebDriverException as e:
        print(f"Brauzerni ishga tushirishda xatolik: {e}")
        exit(1)

def save_to_postgres(conn, url, screenshot_path):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Projects (header, date, image, description) VALUES (%s, %s, %s, %s);",
                ("AI Powered Chatbot", "2025-05-12", screenshot_path, f"Topilgan URL: {url}")
            )
            conn.commit()
            print("Maʼlumot PostgreSQL bazasiga saqlandi.")
    except Exception as e:
        print(f"PostgreSQL saqlashda xatolik: {e}")

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(2)
def take_screenshot(driver, filename):
    path = os.path.join(os.getcwd(), filename)
    scroll_down(driver)
    driver.save_screenshot(path)
    print(f"Skrinshot saqlandi: {path}")
    return path
def collect_links(driver, base_url):
    links = set()
    for tag in driver.find_elements(By.TAG_NAME, "a"):
        href = tag.get_attribute("href")
        if href and href.startswith(base_url):
            links.add(href)
    return links
def crawl(driver, conn, url, visited, target_slug):
    stack = [url]
    while stack:
        current_url = stack.pop()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            driver.get(current_url)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except TimeoutException:
            continue

        if target_slug in current_url:
            print(f"Sahifa topildi: {current_url}")
            screenshot_path = take_screenshot(driver, SCREENSHOT_NAME)
            if conn:
                save_to_postgres(conn, current_url, screenshot_path)
            return True

        links = collect_links(driver, BASE_URL)
        stack.extend(links - visited)

    return False

def main():
    print("Qidiruv boshlandi...")
    print(f"Base URL: {BASE_URL}")
    visited = set()
    driver = init_driver()
    conn = get_connection()

    try:
        create_table_if_not_exists()
        found = crawl(driver, conn, BASE_URL, visited, TARGET_SLUG)
        if not found:
            print(f"Sahifa topilmadi: {TARGET_SLUG}")
    finally:
        driver.quit()
        if conn:
            conn.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Jarayon to‘xtatildi.")
