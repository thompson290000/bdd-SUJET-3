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


Evenement = metadata.tables["Evenement"]
Tour = metadata.tables["Tour"]
Adherent = metadata.tables["Adherent"]
Numero = metadata.tables["Numero"]

database=[]

try :
    database.append((Evenement,1000))
    database.append((Tour,2000))
    database.append((Adherent,1000))
    database.append((Numero,1500))
except KeyError as err:
    print("error : Metadata.tables "+str(err)+" not found")

# product list (permet de generer des noms random dans product_list en bas dans la fonction)
product_list = ["hat", "cap", "shirt", "sweater", "sweatshirt", "shorts",
    "jeans", "sneakers", "boots", "coat", "accessories"]


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

        if self.table.name == "Evenement":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        #Id_Evenement = faker.Id_Evenement(),
                        Gain_total_evenement_adherent = faker.random_int(min=1, max=1500),
                        #email = faker.email(),
                        #address = faker.address(),
                        #dob = faker.date_of_birth(minimum_age=16, maximum_age=60)
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "Tour":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        Id_Evenement = faker.random_int(min=1, max=500), ## sert a generer des noms random dans les entrees
                        Gain_tour_adherent = faker.random_int(min=1, max=1000),
                        Id_Evenement=random.choice(conn.execute(select([Evenement.c.Id_Evenement])).fetchall())[0],  
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "Adherent":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        Nom = faker.random_string(length=11, digits=False),
                        Prenom = faker.first_name(),
                        Gain_total_adherent = faker.random_int(min=1, max=10000),
                        Resultat = faker.boolean(chance_of_getting_true=50),
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "Numero":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    date_obj = datetime.datetime.now() - datetime.timedelta(days=random.randint(0,30))

                    insert_stmt = self.table.insert().values(
                        transaction_date=date_obj.strftime("%Y/%m/%d"),
                        Id_Evenement = faker.random_int(min=1, max=500),
                        Id_Tour = faker.radom_int(min=1, max=500),
                        Libelle_num = faker.random_string(length=15),
                        Id_Adherent = faker.random_int(min=1, max=10000),
                        Id_Tour=random.choice(conn.execute(select([Tour.c.Id_Tour])).fetchall())[0],
                        Id_Tour=random.choice(conn.execute(select([Adherent.c.Id_Adherent])).fetchall())[0],
                    )
                    conn.execute(insert_stmt)


if __name__ == "__main__":
    for i in database:
        generate_data = GenerateData(i)
        generate_data.create_data()
