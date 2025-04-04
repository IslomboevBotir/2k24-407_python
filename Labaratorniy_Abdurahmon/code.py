import time
import psycopg2
from psycopg2 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Database connection parameters
DB_PARAMS = {
    "dbname": "l_db",
    "user": "postgres",
    "password": "Abdurahmon005",
    "host": "localhost",
    "port": "5432"
}

#Publish_data
def convert_date(date_str):
    try:
        if "Obtained:" in date_str:
            date_str = date_str.replace("Obtained:", "").strip()
        return datetime.strptime(date_str, "%B %Y").strftime("%Y-%m-%d")
    except ValueError:
        return None

#Database jo'natish va joylash
def save_to_database(title, description=None, image_url=None, publish_date=None):
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        cursor = connection.cursor()

        # Sana formati tekshiruvi
        formatted_date = convert_date(publish_date) if publish_date else None

        insert_query = '''
        INSERT INTO cres 
        (title, description, image_url, publish_date)
        VALUES (%s, %s, %s, %s);
        '''
        cursor.execute(insert_query, (
            title, description, image_url, formatted_date
        ))
        connection.commit()
        print("Ma'lumotlar muvaffaqiyatli saqlandi")

    except (Exception, Error) as error:
        print(f"Bazaga saqlashda xatolik yuz berdi: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()


#Web site dan ma'lumotlarni olish
def scrape_page(url="https://shaxzodbek.com/", mode="detailed"):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Brauzer ishga tushirildi")

        driver.get(url)
        time.sleep(5)

        #cybersecurity-certification page borish uchun code
        driver.find_element(By.XPATH, "//a[text()='Certifications']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/certifications/cybersecurity-certification/']").click()
        time.sleep(5)
        print("Card opened")

        #Description Olish
        full_description = driver.find_element(By.CLASS_NAME, "certification-description").text.strip()
        description = f"Cybersecurity Certification: {full_description}"

        #Title Olish
        try:
            title = driver.find_element(By.TAG_NAME, "h3").text.strip()
        except:
            title = "Sarlavha topilmadi"

        #Image_url
        try:
            image_url = driver.find_element(By.TAG_NAME, "img").get_attribute("src")
        except:
            image_url = "Rasm topilmadi"

        #Publish_data
        try:
            publish_date = driver.find_element(By.CLASS_NAME, "certification-date").text.strip()
        except:
            publish_date = "Topilmadi"

        # Ma'lumotlarni database saqlash
        save_to_database(
            title=title,
            description=description,
            image_url=image_url,
            publish_date=publish_date
        )


        print("Jarayon yakunlandi")



    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    finally:
        driver.quit()
        print("Brauzer yopildi")


if __name__ == "__main__":
    scrape_page(url="https://shaxzodbek.com/", mode="certification")

