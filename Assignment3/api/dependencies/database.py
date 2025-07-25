from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = "sandwich_maker_api"
USERNAME = "root"
PASSWORD = "19711978Mf@"

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:19711978Mf%40@127.0.0.1:3306/sandwich_maker_api"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from api.models import models
models.Base.metadata.create_all(bind=engine)
