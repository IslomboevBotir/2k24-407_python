from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scraper.posts_scraper import scrape_posts

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        print("Post sahifasidan ma'lumot yig‘ish boshlandi...")
        scrape_posts(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

