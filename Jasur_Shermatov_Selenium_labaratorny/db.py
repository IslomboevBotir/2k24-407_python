from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()


class Certificate(Base):
    __tablename__ = "certificates"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(String, nullable=False)  # Changed from DateTime to String
    image_url = Column(String, nullable=False)
    full_description = Column(Text, nullable=False)


def setup_database():
    engine = create_engine(DB_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine


def save_to_database(certificates, engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for cert in certificates:
            certificate = Certificate(
                title=cert["title"],
                created_at=cert[
                    "created_at"
                ],  # Now directly accepts "YYYY-MM" format as a string
                image_url=cert["image_url"],
                full_description=cert["description"],
            )
            session.add(certificate)
        session.commit()
        print(f"Successfully saved {len(certificates)} certificates to database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
        session.rollback()
    finally:
        session.close()
