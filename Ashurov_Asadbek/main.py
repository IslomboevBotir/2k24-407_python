import time
from datetime import datetime
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from db import Database


class WebScraper:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def navigate_to_target_page(self):
        self.driver.get("https://shaxzodbek.com/")
        self.driver.maximize_window()
        time.sleep(4)

        portfolio_btn = self.driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")
        portfolio_btn.click()
        time.sleep(2)

        pagination_link = self.driver.find_element(
            By.CSS_SELECTOR, "body > main > section > div.pagination > a:nth-child(2)"
        )
        href_value = pagination_link.get_attribute("href")
        self.driver.get(href_value)
        time.sleep(3)

        project_btn = self.driver.find_element(
            By.XPATH, "/html/body/main/section/div[1]/div/div[6]/div[2]/a"
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", project_btn)
        time.sleep(2)
        project_btn.click()
        time.sleep(3)

    def extract_data(self) -> Tuple[str, str, str, str, str]:
        title = self.driver.find_element(By.XPATH, "/html/body/main/section/div/header/h3").text

        raw_text = self.driver.find_element(By.XPATH, "/html/body/main/section/div/header/div/div").text
        date_part = raw_text.split(":")[-1].strip()
        date_obj = datetime.strptime(date_part, "%B %Y")
        created_at = date_obj.strftime("%Y-%m")

        image_url = self.driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div[1]/img"
        ).get_attribute("src")

        image_description = self.driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div[2]"
        ).text

        intro_text = (
            self.driver.find_element(By.XPATH, "/html/body/main/section/div/div[1]/div[2]")
            .text.split("<")[0]
            .strip()
        )
        html_content = self.driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div[2]"
        ).get_attribute("innerHTML")
        all_description = f"{intro_text}\n{html_content}"

        return title, created_at, image_url, image_description, all_description

    def close(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main():
    with Database() as db, WebScraper() as scraper:
        scraper.navigate_to_target_page()
        title, created_at, image_url, image_description, all_description = scraper.extract_data()
        db.insert_data(title, created_at, image_url, image_description, all_description)


if __name__ == "__main__":
    main()