from sqlalchemy import create_engine, MetaData, select
from faker import Faker
import sys
import random
import datetime
import configparser
from connect import engine

engine = engine
metadata = MetaData()
metadata.reflect(bind=engine)

# Instantiate faker object
faker = Faker()
# Instantiate faker frensh object
fakeFR = Faker('fr_FR')

date_obj = datetime.datetime.now() - datetime.timedelta(days=random.randint(0,30))


region = metadata.tables["region"]
protocole = metadata.tables["protocole"]
patient = metadata.tables["patient"]
appliquer = metadata.tables["appliquer"]

database=[]

REGIONS = [
    'Auvergne-Rhône-Alpes',
    'Bourgogne-Franche-Comté',
    'Bretagne',
    'Centre-Val de Loire',
    'Corse',
    'Grand Est',
    'Guadeloupe',
    'Guyane',
    'Hauts-de-France',
    'Île-de-France',
    'La Réunion',
    'Martinique',
    'Normandie',
    'Nouvelle-Aquitaine',
    'Occitanie',
    'Pays de la Loire',
    'Provence-Alpes-Côte d\'Azur',
]


try :
    database.append((region,22))
    database.append((protocole,2000))
    database.append((patient,1000))
    database.append((appliquer,1500))
except KeyError as err:
    print("error : Metadata.tables "+str(err)+" not found")

class GenerateData:
    """
    generate a specific number of records to a target table
    """

    def __init__(self,table):
        """
        initialize command line arguments
        """
        self.table = table[0]
        self.num_records = table[1]


    def create_data(self):
        """
        using faker library, generate data and execute DML
        """

        if self.table.name == "region":
            with engine.begin() as conn:
                for i in REGIONS:
                    insert_stmt = self.table.insert().values(
                        region = i,
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "protocole":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        nom_protocole = fakeFR.cryptocurrency_code(),
                        date_de_mise_en_place_du_protocole = fakeFR.date(),
                        date_de_fin_du_protocole = fakeFR.date()
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "patient":
            date_obj = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        id_region = random.choice(conn.execute(select([region.c.id_region])).fetchall())[0],
                        infecte = random.randint(0, 1),
                        vaccination = random.randint(0, 1),
                        date_de_manifestation = date_obj.strftime("%Y/%m/%d")
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "appliquer":
            with engine.begin() as conn:
                tab = []
                for t in range(self.num_records):
                      tab.append(conn.execute(select([protocole.c.id_protocole])).fetchall()[t][0])
                for _ in range(self.num_records):
                    proto = random.sample(tab,k=1)[0]
                    tab.remove(proto)
                    insert_stmt = self.table.insert().values(
                        id_region=random.choice(conn.execute(select([region.c.id_region])).fetchall())[0],
                        id_protocole=proto,
                    )
                    conn.execute(insert_stmt)


if __name__ == "__main__":
    for i in database:
        generate_data = GenerateData(i)
        generate_data.create_data()
