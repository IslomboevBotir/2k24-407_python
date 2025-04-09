# Jasur_Shermatov_Labaratorny

**Jasur_Shermatov_Labaratorny** 
— bu loyiha Python’ning Selenium kutubxonasi yordamida web scraping (vebdan ma’lumot yig‘ish) uchun mo‘ljallangan. Ma’lumotlar PostgreSQL bazasiga **SQLAlchemy** orqali saqlanadi.

---

## 🧪 Loyiha tuzilmasi

```bash
Jasur_Shermatov_Labaratorny/
├── scraper.py     # Web scraping logikasi (Selenium)
├── db.py          # PostgreSQL bilan bog‘lanish (SQLAlchemy)
├── main.py        # Loyihani ishga tushuruvchi fayl
├── .env           # Muhit o‘zgaruvchilari (database credentials)
├── requirements.txt  # Loyihada ishlatilgan barcha kutubxonalar



DB_HOST=localhost        # Ma’lumotlar bazasi joylashgan host (odatda 'localhost' yoki IP manzili)
DB_PORT=5432             # PostgreSQL porti (standart: 5432)
DB_NAME=labaratorny_db   # Loyihaga tegishli ma’lumotlar bazasi nomi
DB_USER=postgres         # PostgreSQL foydalanuvchi nomi
DB_PASSWORD=postgres     # Foydalanuvchi paroli


Setup your database connection:
and project is ready to use:
do---> python main.py