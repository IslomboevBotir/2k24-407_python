from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from db import save_certification_to_db

def scrape_certification(driver):
    driver.get("https://shaxzodbek.com/")
    sleep(3)

    try:
        cert_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'Certifications')]")
        driver.execute_script("arguments[0].scrollIntoView();", cert_menu)
        sleep(1)
        cert_menu.click()
        sleep(3)
    except Exception as e:
        print(f"Certifications bo'limiga o'tishda xatolik: {e}")
        return

    all_cert_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'certification-card')]")

    ai_cert_card = None
    for card in all_cert_cards:
        title_element = card.find_element(By.XPATH, ".//h4")
        if "AI Engineering Certification" in title_element.text:
            ai_cert_card = card
            break

    if not ai_cert_card:
        print("AI Engineering Certification topilmadi.")
        return

    view_details_btn = None
    selectors = [
        ".//a[contains(text(), 'View Details')]",
        ".//a[contains(@class, 'read-more')]",
        ".//a[contains(@class, 'view-details')]",
        ".//a[text()='View Details →']"
    ]

    for selector in selectors:
        try:
            view_details_btn = ai_cert_card.find_element(By.XPATH, selector)
            if view_details_btn:
                break
        except:
            continue

    if not view_details_btn:
        print("View Details tugmasi topilmadi.")
        return

    driver.execute_script("arguments[0].scrollIntoView();", view_details_btn)
    sleep(1)

    href = view_details_btn.get_attribute("href")
    if href:
        driver.get(href)
    else:
        ActionChains(driver).move_to_element(view_details_btn).click().perform()

    try:
        certification_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header[contains(@class, 'certification-header')]"))
        )
        certification_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'certification-content')]"))
        )

        title = "AI Engineering Certification"
        obtained = ""
        description = ""
        image_url = ""

        for line in certification_header.text.split("\n"):
            if "Obtained:" in line:
                obtained = line.replace("Obtained:", "").strip()

        html_details = certification_content.get_attribute("innerHTML")
        soup = BeautifulSoup(html_details, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        description = paragraphs[0] if paragraphs else ""

        details_dict = {
            "paragraphs": paragraphs,
            "bullets": [li.get_text(strip=True) for li in soup.find_all("li")]
        }

        try:
            image = driver.find_element(By.XPATH,
                                        "//div[contains(@class, 'certification-image')]/img").get_attribute("src")
            image_url = image
        except:
            print("Rasm topilmadi")

        save_certification_to_db(title, obtained, description, image_url, details_dict)

    except Exception as e:
        print(f"To'liq ma'lumotlarni olishda xatolik: {e}")
