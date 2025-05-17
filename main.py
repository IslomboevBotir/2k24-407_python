# main file
from selenium.webdriver.chrome.options import Options
from db import get_connection, create_table_if_not_exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
# DB connection
conn = get_connection()
cursor = conn.cursor()
create_table_if_not_exists()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://shaxzodbek.com/")

try:
    # "Projects" sahifasiga kirish
    projects_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Projects"))
    )
    projects_link.click()

    found = False
    while not found:
        time.sleep(2)
        cards = driver.find_elements(By.CLASS_NAME, "project-content")

        for card in cards:
            if "Job Portal System" in card.text:
                print("Topildi!")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)

                card.find_element(By.PARTIAL_LINK_TEXT, "Job Portal System").click()
                time.sleep(2)
                driver.save_screenshot("./screenshot.png")

                # 🔽 TO‘G‘IRLANGAN XPATHLAR — DOM strukturangizga qarab yangilangan
                header = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//section//header//h3"))
                ).text

                date = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//section//header//div[contains(@class, 'date')]"))
                ).text

                img = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//section//img"))
                ).get_attribute("src")

                desc = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//section//div[contains(@class,'description')]"))
                ).text

                # INSERT
                cursor.execute("""
                    INSERT INTO projects (header, date, image, description)
                    VALUES (%s, %s, %s, %s)
                """, (header, date, img, desc))
                conn.commit()
                print("Job Portal System DB ga muvaffaqiyatli saqlandi")
                found = True
                break

        if not found:
            try:
                next_btn = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                )
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
                time.sleep(1)
                next_btn.click()
            except TimeoutException:
                print("Job Portal System topilmadi")
                break

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
    driver.quit()
