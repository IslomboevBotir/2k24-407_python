from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import psycopg2


def setup_database():
    try:
        conn = psycopg2.connect(
            dbname="lab_r",
            user="postgres",
            password="0940",
            host="localhost",
            port="5433"
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Ma'lumotlar bazasiga ulanishda xatolik: {str(e)}")
        raise


def save_to_database(cursor, conn, title, image, text, publish_date):
    cursor.execute('''
        INSERT INTO post (title, image, text, publish_date)
        VALUES (%s, %s, %s, %s)
    ''', (title, image, text, publish_date))
    conn.commit()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

conn, cursor = setup_database()

try:
    driver.get("https://shaxzodbek.com/")
    time.sleep(2)

    posts_link = driver.find_element(By.LINK_TEXT, "Post")  # "Post" nomli havolani topish
    posts_link.click()
    time.sleep(2)

    next_button = driver.find_element(By.LINK_TEXT, "Next")  # "Next" tugmasini topish
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
    time.sleep(1)
    next_button.click()
    time.sleep(2)

    target_card = driver.find_element(By.XPATH, "//*[contains(text(), 'The Impact of Social Media on Mental Health')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_card)
    time.sleep(1)
    target_card.click()
    time.sleep(2)

    try:
        title = driver.find_element(By.TAG_NAME, "h1").text
    except:
        title = "The Impact of Social Media on Mental Health"  # Agar topilmasa, standart qiymat

    try:
        image = driver.find_element(By.TAG_NAME, "img").get_attribute("src")
    except:
        image = "No image available"

    try:
        sections = driver.find_elements(By.CLASS_NAME, "content-section")
        text = "\n\n".join([section.text.strip() for section in sections if section.text.strip()])
        print(text)
    except Exception as e:
        print("No text available:", e)

    try:
        publish_date = driver.find_element(By.CLASS_NAME, "article-meta").text
    except:
        publish_date = "Unknown"

    save_to_database(cursor, conn, title, image, text, publish_date)
    print("Ma'lumotlar muvaffaqiyatli saqlandi!")

except Exception as e:
    print(f"Xatolik yuz berdi: {str(e)}")

finally:
    conn.close()
    time.sleep(3)
    driver.quit()
# test
