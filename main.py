from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import time
from db import init_database, save_post


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def scrape_ai_post():
    driver = setup_driver()

    try:
        driver.get("https://shaxzodbek.com/")
        time.sleep(4)

        post_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/nav/ul/li[2]/a"))
        )
        post_btn.click()
        time.sleep(2)

        for i in range(2):
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(1)
                try:
                    next_button.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except TimeoutException:
                pass

        read_more_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//h4/a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'the rise of ai in everyday life')]/ancestor::article//a[@class='read-more']"
            ))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", read_more_btn)
        time.sleep(1)
        try:
            read_more_btn.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", read_more_btn)
        time.sleep(3)

        title = driver.find_element(By.XPATH, "//h1[contains(text(), 'The Rise of AI in Everyday Life')]").text

        try:
            date_elem = driver.find_element(By.XPATH, "//div[@class='article-date']")
            publish_date = date_elem.text.strip()
        except:
            publish_date = "March 26, 2025"

        try:
            image_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='The Rise of AI in Everyday Life']"))
            )
            image_url = image_elem.get_attribute("src")
            if image_url.startswith("/"):
                image_url = "https://shaxzodbek.com" + image_url
        except:
            image_url = "Rasm topilmadi"

        try:
            content_section = driver.find_element(By.XPATH, "//div[contains(@class,'content-section')]")
            full_content = content_section.text.strip()
            subtitle = full_content[:200] + "..." if len(full_content) > 200 else full_content
        except:
            full_content = "Artificial Intelligence (AI) is transforming how we work, shop, and interact. From virtual assistants to self-driving cars, AI is becoming a part of our daily routines."
            subtitle = full_content

        save_post(
            title=title,
            subtitle=subtitle,
            image_url=image_url,
            publish_date=publish_date,
            link=driver.current_url,
            full_content=full_content
        )

    except Exception as e:
        pass
    finally:
        driver.quit()


def main():
    init_database()
    scrape_ai_post()


if __name__ == "__main__":
    main()
