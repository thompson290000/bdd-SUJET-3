from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey, Boolean
import configparser
from connect import engine

engine = engine
metadata = MetaData()
metadata.reflect(bind=engine)


# DDL for customers, products, stores, and transactions
region_table = Table(
    "region",
    metadata,
    Column("id_region", Integer, primary_key=True, autoincrement=True),
    Column("region", String(35), nullable=False),
)

protocole_table = Table(
    "protocole",
    metadata,
    Column("id_protocole", Integer, primary_key=True, autoincrement=True),
    Column("nom_protocole", String(35), nullable=False),
    Column("date_de_mise_en_place_du_protocole", Date),
    Column("date_de_fin_du_protocole", Date)
)

patient_table = Table(
    "patient",
    metadata,
    Column("id_client", Integer, primary_key=True, autoincrement=True),
    Column("id_region", ForeignKey("region.id_region"), primary_key=True),
    Column("infecte", Boolean, nullable=True),
    Column("date_de_manifestation", Date),
    Column("vaccination",Boolean)
)

appliquer_table = Table(
    "appliquer",
    metadata,
    Column("id_region", ForeignKey("region.id_region"), primary_key=True),
    Column("id_protocole", ForeignKey("protocole.id_protocole"),primary_key=True)
)

# Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)

    for table in metadata.tables.keys():
        print(f"{table} successfully created")
