from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_utils import wait_to
from database.connection import get_connection
import time

def scrape_posts(driver):
    # Posts jadvalini yaratadi
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title TEXT,
            image TEXT,
            text TEXT,
            publish_date TEXT,
            link TEXT,
            tools_type TEXT,
            full_content TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

    # Saytga kirish
    driver.get("https://shaxzodbek.com/")
    print("Saytga kirdik: https://shaxzodbek.com/")
    time.sleep(3)

    # "Post" sahifasiga o‘tadi
    try:
        # Elementni aniqroq XPath bilan topadi
        posts_link = wait_to(driver, EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Post")]')))
        driver.execute_script("arguments[0].scrollIntoView();", posts_link)  # Element ko‘rinadigan joyga siljitish
        time.sleep(1)
        posts_link.click()
        print("Posts sahifasiga o‘tdik")
        print(f"Joriy URL: {driver.current_url}")
        time.sleep(3)
    except Exception as e:
        print(f"Post sahifasiga o‘tishda xato: {e}")
        print("Sahifa manbasini tekshirish uchun bir qismini chiqarish:")
        print(driver.page_source[:1000])  # Sahifa manbasini tekshirish
        return


    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Posts sahifasini pastga siljitdik")
        time.sleep(3)


    try:
        cards = wait_to(driver, EC.presence_of_all_elements_located((By.CLASS_NAME, "article-grid-card")))
        print(f"Posts sahifasida topilgan kartochkalar soni: {len(cards)}")
    except Exception as e:
        print(f"Posts sahifasida kartochkalarni topishda xato: {e}")
        return

    # Ma'lumotlarni yig‘ish va saqlash uchun
    with open("posts_data.txt", "w", encoding="utf-8") as file:
        for card in cards:
            try:
                title = card.find_element(By.CLASS_NAME, "article-grid-card__title").text
                image_div = card.find_element(By.CLASS_NAME, "article-grid-card__image")
                image = image_div.find_element(By.TAG_NAME, "img").get_attribute("src")
                text = card.find_element(By.CLASS_NAME, "article-grid-card__content").text
                publish_date = card.find_element(By.CLASS_NAME, "article-grid-card__fadedin").text
                link = card.find_element(By.CLASS_NAME, "article-grid-card__title").find_element(By.TAG_NAME, "a").get_attribute("href")
                tools_type = "Yo‘q"


                full_content = ""
                if title == "AI Search Engines Challenging Google":
                    try:
                        driver.get(link)
                        print(f"Ichki sahifaga o‘tdik: {link}")
                        time.sleep(3)

                        # Ichki sahifadan to‘liq matnni yig‘ib oladi
                        content = wait_to(driver, EC.presence_of_element_located((By.CLASS_NAME, "post-content")))
                        full_content = content.text

                        # Asosiy sahifaga qaytadi
                        driver.get("https://shaxzodbek.com/post/")
                        time.sleep(3)
                    except Exception as e:
                        print(f"Ichki sahifadan ma'lumot olishda xato: {e}")
                        full_content = "Ma'lumot topilmadi"

                # Ma'lumotlarni faylga yozish uchun
                file.write(f"Title: {title}\n")
                file.write(f"Image: {image}\n")
                file.write(f"Text: {text}\n")
                file.write(f"Publish Date: {publish_date}\n")
                file.write(f"Link: {link}\n")
                file.write(f"Tools Type: {tools_type}\n")
                if full_content:
                    file.write(f"Full Content: {full_content}\n")
                file.write("-" * 50 + "\n")

                # Ma'lumotlarni PostgreSQL’ga yozadi
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO posts (title, image, text, publish_date, link, tools_type, full_content)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (title, image, text, publish_date, link, tools_type, full_content))
                conn.commit()
                cursor.close()
                conn.close()

                print(f"Posts - Title: {title}")
                print(f"Posts - Image: {image}")
                print(f"Posts - Text: {text}")
                print(f"Posts - Publish Date: {publish_date}")
                print(f"Posts - Link: {link}")
                print(f"Posts - Tools Type: {tools_type}")
                if full_content:
                    print(f"Posts - Full Content: {full_content}")
                print("-" * 50)

            except Exception as e:
                print(f"Posts sahifasida kartochkadan ma'lumot olishda xato: {e}")