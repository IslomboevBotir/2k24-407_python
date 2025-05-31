from selenium.webdriver.common.by import By
from time import sleep
from utils.parser import parse_certification_html

def scrape_certification(driver):
    driver.get("https://shaxzodbek.com/")
    sleep(2)

    # Certifications bo'limini topamiz va unga o'tamiz
    cert_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'Certifications')]")
    driver.execute_script("arguments[0].scrollIntoView();", cert_menu)
    sleep(1)
    cert_menu.click()
    sleep(2)

    # Kerakli kartani topamiz
    all_cert_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'certification-card')]")
    target_card = None

    for card in all_cert_cards:
        try:
            title_element = card.find_element(By.XPATH, ".//h4/a")
            if "Cybersecurity Certification" in title_element.text:
                target_card = card
                break
        except:
            continue

    if target_card:
        details_link = target_card.find_element(By.XPATH, ".//a[contains(@class, 'read-more')]")
        href = details_link.get_attribute("href")
        full_url = f"https://shaxzodbek.com{href}" if href.startswith("/") else href
        print(f"🔗 URL topildi: {full_url}")

        driver.get(full_url)
        sleep(2)

        # Sahifa kodini oling
        html = driver.page_source

        # Parse qilamiz
        return parse_certification_html(html)
    else:
        print("❌ 'Cybersecurity Certification' topilmadi.")
        return None, None, None, None, None
