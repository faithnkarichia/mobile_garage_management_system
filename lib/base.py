# bess
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base= declarative_base()
engine= create_engine("sqlite:///mobile_garage.db")
Session= sessionmaker(bind=engine)
session=Session()