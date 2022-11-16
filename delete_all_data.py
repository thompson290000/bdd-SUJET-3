from sqlalchemy import create_engine, MetaData, Column, Integer, Numeric, String, Date, Table, ForeignKey
from sqlalchemy.sql import text
import configparser
from connect import engine
import contextlib



def delete_all_data(engine,metadata):
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(metadata.sorted_tables):
            print (table.delete())
            statement=text("ALTER TABLE "+table.name+" AUTO_INCREMENT = 0")
            con.execute(table.delete())
            con.execute(statement)
        trans.commit()


engine = engine
metadata = MetaData()
metadata.reflect(bind=engine)

delete_all_data(engine,metadata)
