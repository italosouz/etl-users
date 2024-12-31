from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Integer, Date, DateTime
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    fare = Column(Float, nullable=False)
    gender = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now)   