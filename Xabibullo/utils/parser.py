from bs4 import BeautifulSoup


def parse_certification_html(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1").text.strip() if soup.find("h1") else "Cybersecurity Certification"

    obtained_text = soup.find(string=lambda s: "Obtained" in s)
    obtained = obtained_text.split(":")[1].strip() if obtained_text else ""

    image = soup.find("img")
    image_url = image["src"] if image else ""

    description_tag = soup.find("p")
    description = description_tag.text.strip() if description_tag else ""

    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    bullets = [li.get_text(strip=True) for li in soup.find_all("li")]

    details_dict = {
        "paragraphs": paragraphs,
        "bullets": bullets
    }

    return title, obtained, description, image_url, details_dict
