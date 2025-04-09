import asyncio
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


async def scrape_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://shaxzodbek.com/")
    driver.set_window_size(1024, 1440)
    await asyncio.sleep(2)

    btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")
    btn.click()
    await asyncio.sleep(4)

    element = driver.find_element(
        By.CSS_SELECTOR, "body > main > section > div.pagination > a:nth-child(3)"
    )
    href_value = element.get_attribute("href")
    driver.get(href_value)
    await asyncio.sleep(3)

    btn = driver.find_element(
        By.XPATH, "/html/body/main/section/div[1]/div/div[1]/div[2]/a"
    )
    btn.click()
    await asyncio.sleep(3)

    title = driver.find_element(By.XPATH, "/html/body/main/section/div/header/h3").text
    created_at = datetime.strptime(
        driver.find_element(By.XPATH, "/html/body/main/section/div/header/div/div")
        .text.split(":")[-1]
        .strip(),
        "%B %Y",
    ).strftime("%Y-%m")
    image_url = driver.find_element(
        By.XPATH, "/html/body/main/section/div/div[1]/div[1]/img"
    ).get_attribute("src")

    try:
        intro_text = (
            driver.find_element(By.XPATH, "/html/body/main/section/div/div[1]/div[2]")
            .text.split("<")[0]
            .strip()
        )
        html_content = driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div[2]"
        ).get_attribute("innerHTML")
        full_description = f"{intro_text}\n{html_content}"
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        full_description = driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div[2]"
        ).get_attribute("innerHTML")

    certificate_data = {
        "title": title,
        "created_at": created_at,
        "image_url": image_url,
        "description": full_description,
    }

    driver.quit()
    return [certificate_data]

async def main():
    data = await scrape_data()
    print(data)

if __name__ == "__main__":
    asyncio.run(main())