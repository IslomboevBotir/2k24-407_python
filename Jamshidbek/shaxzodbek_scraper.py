from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import psycopg2
from datetime import datetime
import os

# PostgreSQL bog'lanish uchun ma'lumotlar
DB_NAME = "shaxzodbek_data"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"


def setup_chrome_driver():
    """Chrome driver sozlash"""
    options = Options()
    options.add_argument("--headless")  # Brauzer oynasini ko'rsatmaslik (ixtiyoriy)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver


def setup_database():
    """PostgreSQL bazasini tayyorlash"""
    try:
        # Bazaga ulanish
        conn = psycopg2.connect(
            dbname='shaxzodbek_data',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Jadvallarni yaratish
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS posts
                       (
                           id
                           SERIAL
                           PRIMARY
                           KEY,
                           title
                           VARCHAR
                       (
                           255
                       ),
                           image_url TEXT,
                           content TEXT,
                           publish_date VARCHAR
                       (
                           100
                       ),
                           link TEXT,
                           category VARCHAR
                       (
                           50
                       )
                           );
                       """)

        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS projects
                       (
                           id
                           SERIAL
                           PRIMARY
                           KEY,
                           title
                           VARCHAR
                       (
                           255
                       ),
                           image_url TEXT,
                           content TEXT,
                           publish_date VARCHAR
                       (
                           100
                       ),
                           link TEXT,
                           tools_type VARCHAR
                       (
                           100
                       )
                           );
                       """)

        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS certifications
                       (
                           id
                           SERIAL
                           PRIMARY
                           KEY,
                           title
                           VARCHAR
                       (
                           255
                       ),
                           image_url TEXT,
                           content TEXT,
                           publish_date VARCHAR
                       (
                           100
                       ),
                           link TEXT
                           );
                       """)

        print("Bazada jadvallar muvaffaqiyatli yaratildi!")
        return conn
    except Exception as e:
        print(f"Bazaga ulanishda xatolik: {e}")
        return None


def extract_card_data(card, category):
    """Kartochkadan ma'lumotlarni ajratib olish"""
    data = {"category": category}

    try:
        # Sarlavha
        title_elem = card.find_element(By.CSS_SELECTOR, "h3, h2")
        data["title"] = title_elem.text.strip() if title_elem else ""
    except NoSuchElementException:
        data["title"] = ""

    try:
        # Rasm
        img_elem = card.find_element(By.TAG_NAME, "img")
        data["image_url"] = img_elem.get_attribute("src") if img_elem else ""
    except NoSuchElementException:
        data["image_url"] = ""

    try:
        # Matn
        content_elem = card.find_element(By.CSS_SELECTOR, "p, .card-text")
        data["content"] = content_elem.text.strip() if content_elem else ""
    except NoSuchElementException:
        data["content"] = ""

    try:
        # Sana
        date_elem = card.find_element(By.CSS_SELECTOR, ".date, .publish-date, small")
        data["publish_date"] = date_elem.text.strip() if date_elem else ""
    except NoSuchElementException:
        data["publish_date"] = ""

    try:
        # Havola
        link_elem = card.find_element(By.TAG_NAME, "a")
        data["link"] = link_elem.get_attribute("href") if link_elem else ""
    except NoSuchElementException:
        data["link"] = ""

    # Loyihalar sahifasi uchun asbob turi
    if category == "projects":
        try:
            tools_elem = card.find_element(By.CSS_SELECTOR, ".tools, .badge, .tags")
            data["tools_type"] = tools_elem.text.strip() if tools_elem else ""
        except NoSuchElementException:
            data["tools_type"] = ""

    return data


def save_to_database(conn, data):
    """Ma'lumotlarni bazaga saqlash"""
    if not conn:
        print("Bazaga ulanish mavjud emas!")
        return False

    try:
        cursor = conn.cursor()
        category = data.pop("category")

        if category == "posts":
            cursor.execute("""
                           INSERT INTO posts (title, image_url, content, publish_date, link, category)
                           VALUES (%s, %s, %s, %s, %s, %s)
                           """, (data["title"], data["image_url"], data["content"],
                                 data["publish_date"], data["link"], data.get("category", "")))

        elif category == "projects":
            cursor.execute("""
                           INSERT INTO projects (title, image_url, content, publish_date, link, tools_type)
                           VALUES (%s, %s, %s, %s, %s, %s)
                           """, (data["title"], data["image_url"], data["content"],
                                 data["publish_date"], data["link"], data.get("tools_type", "")))

        elif category == "certifications":
            cursor.execute("""
                           INSERT INTO certifications (title, image_url, content, publish_date, link)
                           VALUES (%s, %s, %s, %s, %s)
                           """, (data["title"], data["image_url"], data["content"],
                                 data["publish_date"], data["link"]))

        return True
    except Exception as e:
        print(f"Ma'lumotni bazaga saqlashda xatolik: {e}")
        return False


def save_to_text_file(data, category):
    """Ma'lumotlarni matn fayliga saqlash"""
    try:
        # Papkani yaratish (mavjud bo'lmasa)
        if not os.path.exists("../shaxzodbek_data"):
            os.makedirs("../shaxzodbek_data")

        # Fayl nomi yaratish
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"shaxzodbek_data/{category}_{timestamp}.txt"

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Kategoriya: {category}\n")
            file.write(f"Sarlavha: {data.get('title', '')}\n")
            file.write(f"Rasm URL: {data.get('image_url', '')}\n")
            file.write(f"Matn: {data.get('content', '')}\n")
            file.write(f"Chop etilgan sana: {data.get('publish_date', '')}\n")
            file.write(f"Havola: {data.get('link', '')}\n")

            if category == "projects" and "tools_type" in data:
                file.write(f"Asbob turi: {data.get('tools_type', '')}\n")

            file.write("\n" + "-" * 50 + "\n\n")

        print(f"Ma'lumot muvaffaqiyatli saqlandi: {filename}")
        return True
    except Exception as e:
        print(f"Faylga saqlashda xatolik: {e}")
        return False


def scrape_page(driver, url, category, conn):
    """Sahifadan ma'lumotlarni yig'ish"""
    try:
        print(f"{category} sahifasi ochilmoqda: {url}")
        driver.get(url)

        # Sahifa to'liq yuklanishi uchun kutish
        time.sleep(3)

        # Card elementlarini topish
        # Shaxzodbek saytidagi kartochkalar turli xil CSS selektorlarda bo'lishi mumkin
        card_selectors = [
            ".card", ".post-card", ".project-card", ".certification-card",
            ".item", "article", ".col-md-4", ".col-lg-3", ".blog-item"
        ]

        cards = []
        for selector in card_selectors:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                cards = elements
                print(f"{len(cards)} ta {category} kartochkalari topildi ({selector} selektori bilan)")
                break

        if not cards:
            print(f"{category} sahifasida kartochkalar topilmadi")
            return []

        results = []
        for card in cards:
            data = extract_card_data(card, category)
            results.append(data)

            # Ma'lumotlarni saqlash
            save_to_text_file(data, category)
            if conn:
                save_to_database(conn, data.copy())

        return results
    except Exception as e:
        print(f"{category} sahifasidan ma'lumot yig'ishda xatolik: {e}")
        return []


def main():
    """Asosiy funksiya"""
    # Chrome driver-ni tayyorlash
    driver = setup_chrome_driver()

    # Bazaga ulanish
    conn = setup_database()

    # Shaxzodbek saytining asosiy URL manzili
    base_url = "https://shaxzodbek.com"  # Bu URL o'zgarishi mumkin
    pages = {
        "posts": f"{base_url}/blog",
        "projects": f"{base_url}/projects",
        "certifications": f"{base_url}/certifications"
    }
    # Sahifalarga kirish va ma'lumotlarni yig'ish
    pages = {
        "posts": f"{base_url}/blog",  # Maqolalar sahifasi
        "projects": f"{base_url}/projects",  # Loyihalar sahifasi
        "certifications": f"{base_url}/certifications"  # Sertifikatlar sahifasi
    }

    all_data = {}
    for category, url in pages.items():
        print(f"\n{category.upper()} sahifasi tahlil qilinmoqda...")
        results = scrape_page(driver, url, category, conn)
        all_data[category] = results

        print(f"{len(results)} ta {category} ma'lumotlari yig'ildi")

    # Chrome driver-ni yopish
    driver.quit()

    # PostgreSQL ulanishni yopish
    if conn:
        conn.close()
        print("PostgreSQL ulanishi yopildi")

    # Natijalarni ko'rsatish
    for category, items in all_data.items():
        print(f"\n{category.upper()}: {len(items)} ta")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item.get('title', 'Sarlavhasiz')}")

    print("\nMa'lumotlar muvaffaqiyatli yig'ildi va saqlandi!")


if __name__ == "__main__":
    main()
