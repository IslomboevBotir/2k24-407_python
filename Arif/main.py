from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from db.database import DatabaseManager
from scraper.certification_scraper import CertificationScraper
from config import DB_CONFIG, SCRAPER_CONFIG


def main():
    db_manager = DatabaseManager(DB_CONFIG)
    db_manager.connect()
    if not db_manager.conn or not db_manager.cursor:
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--minimize-window")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    scraper = CertificationScraper(driver, wait_timeout=SCRAPER_CONFIG["wait_timeout"])

    try:
        result = scraper.scrape(
            navigation=SCRAPER_CONFIG["navigation"],
            card_class_name=SCRAPER_CONFIG["card_class_name"],
            card_title=SCRAPER_CONFIG["card_title"],
        )

        db_manager.save_certification(result)

    finally:
        db_manager.close()


if __name__ == "__main__":
    main()
