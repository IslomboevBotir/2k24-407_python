from scraper.browser import get_chrome_driver
from scraper.cert_scraper import scrape_certification
from db.database import create_table_if_not_exists, save_certification_to_db

def main():
    create_table_if_not_exists()

    driver = get_chrome_driver()
    try:
        print("🌐 Saytga kirilmoqda...")
        title, obtained, description, image_url, details_dict = scrape_certification(driver)

        if title:
            save_certification_to_db(title, obtained, description, image_url, details_dict)
        else:
            print("❌ Ma'lumot topilmadi, saqlanmadi.")

    except Exception as e:
        print(f"❌ Umumiy xatolik: {e}")

    finally:
        driver.quit()
        print("🚪 Brauzer yopildi.")

if __name__ == "__main__":
    main()
