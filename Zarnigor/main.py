from selenium.webdriver.chrome.options import Options
from db import get_connection, create_table_if_not_exists
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = Options()

conn = get_connection()
cursor = conn.cursor()
create_table_if_not_exists()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://shaxzodbek.com/")

try:
    certifications_link = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Certifications"))
    )
    certifications_link.click()

    found = False
    while not found:
        time.sleep(2)
        cards = driver.find_elements(By.CLASS_NAME, "certification-content")

        for card in cards:
            if "Game Development Certification" in card.text:
                print("Found")
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)

                card.find_element(By.LINK_TEXT, "Game Development Certification").click()
                # driver.save_screenshot("./screenshot.png")
                time.sleep(5)

                styled_block = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'border:2px solid #8E44AD')]"))
                )

                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                      styled_block)
                time.sleep(1)
                screenshot_path = "game_dev_cert_block.png"
                styled_block.screenshot(screenshot_path)

                header = styled_block.find_element(By.TAG_NAME, "h2").text
                desc = styled_block.find_element(By.TAG_NAME, "ul").text
                footer_line = styled_block.find_elements(By.TAG_NAME, "p")[-1].text  # for the last <p>

                date = "2025-05-24"

                cursor.execute("""
                    INSERT INTO certifications (header, date, image, description)
                    VALUES (%s, %s, %s, %s)
                """, (header, date, screenshot_path, desc + "\n" + footer_line))
                conn.commit()
                print("✅ Game Development Certification info saved correctly.")

                conn.commit()
                time.sleep(2)
                found = True
                break

        if not found:
            try:
                next_btn = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                )
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_btn)
                time.sleep(1)
                next_btn.click()
            except TimeoutException:
                print("Game Development Certification not found")
                break

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
    driver.quit()