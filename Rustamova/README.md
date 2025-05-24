# Scraper Project

Ushbu loyiha veb saytlardan ma'lumotlarni avtomatik tarzda yig‘ib, PostgreSQL bazasiga saqlash uchun yozilgan. Python va BeautifulSoup kutubxonalari asosida ishlaydi.

Loyiha tuzilmasi

```
scraper_project/
│
├── main.py              # Dasturning kirish nuqtasi
├── scraper.py           # Scraping (ma'lumotlarni yig‘ish) funksiyalari
├── db.py                # PostgreSQL bilan ishlovchi funksiya va metodlar
├── config.py            # Konfiguratsiya: DB sozlamalari
├── requirements.txt     # Kerakli Python kutubxonalar ro‘yxati
└── README.md            # Ushbu hujjat
```

Talablar

```bash
pip install -r requirements.txt
```

Yoki alohida ko‘rsating:

- requests  
- beautifulsoup4  
- psycopg2

Ishga tushirish

1. `config.py` faylida DB sozlamalarni to‘ldiring:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "scraper_db",
    "user": "postgres",
    "password": "your_password"
}
```

2. Loyihani quyidagicha ishga tushiring:

```bash
python main.py
```

Ma'lumotlar bazasi

Loyiha PostgreSQL bilan ishlaydi. `db.py` faylida jadval yaratish, ma'lumot qo‘shish funksiyalari mavjud.

Texnologiyalar

- Python 3.x  
- BeautifulSoup  
- Requests  
- PostgreSQL  
- Psycopg2

Test

Hozirda avtomatik testlar mavjud emas. Dasturni `main.py` orqali ishga tushirib, terminalda natijalarni tekshirish mumkin. 
Eslatma

Har doim scraping qilayotgan saytning `robots.txt` faylini tekshiring. Veb saytlar scrapingga ruxsat bermagan bo‘lishi mumkin.


