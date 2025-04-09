import asyncio
from scraper import scrape_data
from db import setup_database, save_to_database

async def main():
    print("Setting up database...")
    engine = setup_database()

    print("Scraping certificate data...")
    certificates = await scrape_data()  # await qilish kerak

    if certificates:
        print(f"Found {len(certificates)} certificates to save")
        save_to_database(certificates, engine)
    else:
        print("No certificates found to save")

    print("Process completed.")

if __name__ == "__main__":
    asyncio.run(main())