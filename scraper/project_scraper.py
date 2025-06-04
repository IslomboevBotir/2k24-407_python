from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config.settings import FIREFOX_CONFIG
from database.insert import save_project_to_db
from utils.wait_utils import wait, scroll_to
import time

def get_driver():
    service = Service(FIREFOX_CONFIG["gecko_path"])
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--incognito")
    
    return webdriver.Firefox(service=service, options=options)

def scrape_fitness_tracker():
    driver = get_driver()
    try:
        driver.get("https://shaxzodbek.com/")
        wait(3)

        projects_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'Projects')]")
        scroll_to(driver, projects_menu)
        projects_menu.click()
        wait(3)

        cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'project-card')]")
        fitness_card = None
        for card in cards:
            title = card.find_element(By.XPATH, ".//h3").text
            if "Fitness Tracker App" in title:
                fitness_card = card
                break

        if not fitness_card:
            print("❌ Fitness Tracker App topilmadi.")
            return

        view_btn = fitness_card.find_element(By.XPATH, ".//a[contains(text(), 'Details')]")
        scroll_to(driver, view_btn)
        ActionChains(driver).move_to_element(view_btn).click().perform()
        wait(3)

        header = driver.find_element(By.CLASS_NAME, "project-header")
        title = header.find_element(By.TAG_NAME, "h1").text.strip()
        date = header.find_element(By.CLASS_NAME, "project-date").text.strip()
        badges = [b.text for b in header.find_elements(By.CLASS_NAME, "type-badge")]

        try:
            image_url = driver.find_element(By.CLASS_NAME, "project-featured-image").find_element(By.TAG_NAME, "img").get_attribute("src")
        except:
            image_url = ""

        desc_div = driver.find_element(By.CLASS_NAME, "project-description")
        description = desc_div.text.strip()

        tech_elements = driver.find_elements(By.CLASS_NAME, "technology-item")
        technologies = [t.find_element(By.TAG_NAME, "span").text.strip() for t in tech_elements]

        links = driver.find_elements(By.XPATH, "//div[@class='project-links']/a")
        project_links = {}
        for link in links:
            text = link.text.strip()
            href = link.get_attribute("href")
            if "GitHub" in text:
                project_links["github"] = href
            elif "Live Demo" in text:
                project_links["live_demo"] = href

        save_project_to_db(title, date, description, image_url, badges, technologies, project_links)

    except Exception as e:
        print(f"❌ Scraper error: {e}")
    finally:
        wait(2)
        driver.quit()
