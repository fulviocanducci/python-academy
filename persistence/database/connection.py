from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from urllib.parse import quote_plus
from constants import DB_HOST
from constants import DB_USER
from constants import DB_PASSWORD
from constants import DB_NAME

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)

engine = create_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass