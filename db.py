from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI
from sqlalchemy import Column, Integer, String

engine = create_engine(DATABASE_URI, echo=True, encoding='utf-8')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100))
    url = Column(String(200))
    subs = Column(Integer())


if __name__ == '__main__':
    Items.__table__.create(engine)
