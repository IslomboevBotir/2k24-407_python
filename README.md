AI Post Scraper
Bu loyiha veb-saytdan ("https://shaxzodbek.com/") AI bilan bog'liq postlarni yig'ib, ularni SQLite ma'lumotlar bazasida saqlaydi. Selenium yordamida veb-sahifalarni avtomatik ravishda boshqaradi va ma'lumotlarni (sarlavha, subtitr, rasm URL, nashr sanasi, havola va to'liq matn) saqlaydi.
Talablar
Loyihani ishlatish uchun quyidagi kutubxonalar o'rnatilgan bo'lishi kerak:

Python 3.8 yoki undan yuqori
selenium
webdriver_manager
sqlite3 (Python bilan birga keladi)

O'rnatish

Loyihani klonlang:
git clone https://github.com
cd sizning-repo-nomi


Virtual muhitni yarating va faollashtiring:
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate


Kerakli kutubxonalarni o'rnating:
pip install selenium webdriver_manager


Chrome brauzeri va ChromeDriver o'rnatilgan bo'lishi kerak. webdriver_manager ChromeDriver-ni avtomatik yuklaydi.


Loyiha tuzilmasi

scraper.py: Veb-saytdan ma'lumotlarni yig'uvchi asosiy skript.
db.py: SQLite ma'lumotlar bazasini boshqarish uchun funksiyalar.
posts.db: Yig'ilgan ma'lumotlar saqlanadigan SQLite fayli (avtomatik yaratiladi).

Foydalanish

Loyihani ishga tushurish uchun scraper.py faylini ishga tushuring:
python scraper.py


Skript quyidagi amallarni bajaradi:

"https://shaxzodbek.com/" saytiga kiradi.
"Posts" bo'limiga o'tadi va "Next" tugmasini ikki marta bosadi.
"The Rise of AI in Everyday Life" nomli postni topadi.
Postning sarlavhasi, subtitri, rasm URL, nashr sanasi, havola va to'liq matnini yig'adi.
Ma'lumotlarni posts.db fayliga saqlaydi.


Saqlangan ma'lumotlarni ko'rish uchun db.py dagi get_all_posts() funksiyasidan foydalaning:
from db import get_all_posts
posts = get_all_posts()
for post in posts:
    print(post)



Eslatmalar

Internet aloqasi barqaror bo'lishi kerak.
Agar sayt tuzilmasi o'zgarsa, XPath so'rovlarini yangilash kerak bo'lishi mumkin.
Har safar skript ishga tushganda eski posts.db fayli o'chiriladi va yangisi yaratiladi.

# Selenium_Lab
