from sqlalchemy import create_engine, MetaData, Column, Integer, Numeric, String, Date, Table, ForeignKey
from connect import engine

engine = engine
metadata = MetaData()
metadata.reflect(bind=engine)

metadata.drop_all(engine)
