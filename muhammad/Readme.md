# Labaratorniy_Abdurahmon

Ushbu loyiha `Selenium` kutubxonasi yordamida web sahifadan ma'lumotlarni yig‘adi va `PostgreSQL` bazasiga saqlaydi.

## Asosiy texnologiyalar:
- Python
- Selenium
- PostgreSQL
- psycopg2
- WebDriver Manager

## Loyihaning vazifasi:
Shaxzodbek.com saytidan `Cybersecurity Certification` sahifasidagi ma'lumotlarni (sarlavha, ta'rif, rasm havolasi va chop etilgan sanasi) olib, ma'lumotlar bazasiga saqlaydi.

## Bazada ishlatiladigan jadval:

Loyiha quyidagi `cres` nomli jadvalga ma'lumot saqlaydi:

```sql
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    image_url TEXT,
    publish_date DATE
);