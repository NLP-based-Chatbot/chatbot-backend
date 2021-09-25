import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import re

uri = os.getenv("DATABASE_URL")  # or other relevant config var
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

if uri==None or uri=="":
    engine = create_engine("postgresql://wingmanuser:wingmanuser@localhost:5432/hospital_demo", echo=False)
    #engine = create_engine("postgresql://lezkthpysqsmok:59a647db86f9a0ef9909edfaa3d8396cf75274a2956a45fc127ae06864ebf637@ec2-44-198-151-32.compute-1.amazonaws.com:5432/dd5nbunbcg2ar8", echo=False)
    print("DB connection success")
else:
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        engine = create_engine(uri)
        print("DB connection success")
        
        
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Doctor(Base):
    
    __tablename__ = "doctor"
    
    doctor_id   =   Column(String(20),primary_key=True)
    initials    =   Column(String(10))
    first_name  =   Column(String(30))
    last_name   =   Column(String(40))
    