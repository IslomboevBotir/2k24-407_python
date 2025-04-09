from scraper import scrape_data
from db import setup_database, save_to_database


def main():
    print("Setting up database...")
    engine = setup_database()

    print("Scraping certificate data...")
    certificates = scrape_data()

    if certificates:
        print(f"Found {len(certificates)} certificates to save")
        save_to_database(certificates, engine)
    else:
        print("No certificates found to save")

    print("Process completed.")


if __name__ == "__main__":
    main()
