import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import TimeoutException


class CertificationScraper:
    def __init__(self, driver, wait_timeout=2):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.collected_data = {}
        self.extra_description = {}

    def _click_navigation(self, navigation):
        self.driver.get("https://shaxzodbek.com")
        certifications_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, navigation))
        )
        certifications_link.click()

    def _find_and_click_card(self, card_class_name, card_title):
        found = False
        while not found:
            cards = self.driver.find_elements(By.CLASS_NAME, card_class_name)

            for card in cards:
                if card_title in card.text:
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                        card,
                    )
                    sleep(1)
                    link = self.wait.until(
                        EC.element_to_be_clickable((By.LINK_TEXT, card_title))
                    )
                    link.click()
                    return True

            if not found:
                try:
                    next_btn = self.wait.until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                    )
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                        next_btn,
                    )
                    next_btn.click()
                except TimeoutException:
                    return False
        return False

    def _collect_data(self):
        self.collected_data["title"] = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//main/section/div/header/h3"))
        ).text

        self.collected_data["date"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/header/div/div")
            )
        ).text

        self.collected_data["image_url"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[1]/img")
            )
        ).get_attribute("src")

        self.collected_data["description"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]")
            )
        ).text

        self.extra_description["header"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/h2")
            )
        ).text

        self.extra_description["description"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/p[1]")
            )
        ).text

        self.extra_description["design_tools"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/ul/li[1]")
            )
        ).text

        self.extra_description["user_research"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/ul/li[2]")
            )
        ).text

        self.extra_description["prototyping"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/ul/li[3]")
            )
        ).text

        self.extra_description["footer"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//main/section/div/div[1]/div[2]/div/p[2]")
            )
        ).text

        self.extra_description_json = json.dumps(self.extra_description)

        self.collected_data["extra_description"] = self.extra_description_json

    def scrape(self, navigation, card_class_name, card_title):
        try:
            self._click_navigation(navigation)
            if self._find_and_click_card(card_class_name, card_title):
                self._collect_data()
                print(self.collected_data)
                return self.collected_data
            else:
                print("Certification not found")
                return None

        except Exception as e:
            print("Error:", e)
            return None

        finally:
            self.driver.quit()
