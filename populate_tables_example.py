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


customers = metadata.tables["customers"]
products = metadata.tables["products"]
stores = metadata.tables["stores"]
transactions = metadata.tables["transactions"]

database=[]

try :
    database.append((customers,1000))
    database.append((products,2000))
    database.append((stores,1000))
    database.append((transactions,1500))
except KeyError as err:
    print("error : Metadata.tables "+str(err)+" not found")

# product list
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

        if self.table.name == "customers":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        first_name = faker.first_name(),
                        last_name = faker.last_name(),
                        email = faker.email(),
                        address = faker.address(),
                        dob = faker.date_of_birth(minimum_age=16, maximum_age=60)
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "products":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        name = random.choice(product_list),
                        price = faker.random_int(1,100000) / 100.0
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "stores":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = self.table.insert().values(
                        address = faker.address()
                    )
                    conn.execute(insert_stmt)

        if self.table.name == "transactions":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    date_obj = datetime.datetime.now() - datetime.timedelta(days=random.randint(0,30))

                    insert_stmt = self.table.insert().values(
                        transaction_date=date_obj.strftime("%Y/%m/%d"),
                        customer_id=random.choice(conn.execute(select([customers.c.customer_id])).fetchall())[0],
                        product_id=random.choice(conn.execute(select([products.c.product_id])).fetchall())[0],
                        store_id=random.choice(conn.execute(select([stores.c.store_id])).fetchall())[0]
                    )
                    conn.execute(insert_stmt)


if __name__ == "__main__":
    for i in database:
        generate_data = GenerateData(i)
        generate_data.create_data()
