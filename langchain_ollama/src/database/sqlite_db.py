from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_USER = 'postgres'
DB_PASSWORD = 'admin'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME='fastapi'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_PASSWORD}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

