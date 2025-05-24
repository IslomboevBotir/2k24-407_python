from config import get_driver
from scraper import scrape_certification
from time import sleep

def main():
    driver = get_driver()
    try:
        scrape_certification(driver)
    finally:
        sleep(2)
        driver.quit()

if __name__ == "__main__":
    main()
