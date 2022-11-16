import sqlalchemy
import contextlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import MetaData
import getpass
import sys
import configparser

config=configparser.ConfigParser()
config.read('connect.conf')
user=config['SETTINGS']['User']
password=config['SETTINGS']['Password']
database=config['SETTINGS']['Database']
port=config['SETTINGS']['Port']


try:
  global engine;
  engine = sqlalchemy.create_engine("mariadb+mariadbconnector://"+user+":"+password+"@127.0.0.1:"+port+"/"+database)


except Exception as error:
    print('Engine error : ',error)
else:
    print("connection success !")
