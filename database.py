from datetime import datetime
from sqlalchemy.orm import backref, sessionmaker,declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Float, create_engine


SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} # This parameter is only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create base class for declaring tables
Base = declarative_base()



class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,autoincrement=True)
    description = Column(String())
    amount = Column(Float())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()