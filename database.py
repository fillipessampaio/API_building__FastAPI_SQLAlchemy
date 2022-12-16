from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///db.sqlite3"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
'''
"connect_args={"check_same_thread": False}" só é necessário quando estamos utilizando o SQLite.
'''

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
