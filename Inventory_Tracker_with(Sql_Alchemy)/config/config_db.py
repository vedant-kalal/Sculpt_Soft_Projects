from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:vedank10@localhost:3306/inventory_tracker_sqlalchemy", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Aliases for easy access
column = Column
integer = Integer
st = String
fl = Float
