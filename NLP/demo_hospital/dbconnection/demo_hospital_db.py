import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,Time,Date
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
    
    doctor_id   =   Column(String(30),primary_key=True)
    initials    =   Column(String(10))
    first_name  =   Column(String(30))
    last_name   =   Column(String(30))


class Appiontment(Base):

    __tablename__ = "appointments"

    appointment_id  = Column(String(30),primary_key=True)
    doctor_id       = Column(String(30))
    cust_id         = Column(String(30))
    time_slot       = Column(Time())
    date            = Column(Date())

class DoctorAvailable(Base):

    __tablename__ = "doctor_availability"

    docotr_id       = Column(String(30))
    day_of_week     = Column(String(10))
    time            = Column(Time())


class DoctorSpec(Base):

    __tablename__ = "doctor_specialization"

    doctor_id   = Column(String(30))
    spec_id     = Column(String(10))


class Specialization(Base):

    __tablename__ = "specs"

    spec_id     = Column(String(10),primary_key=True)
    spec_name   = Column(String(30))

class Patient(Base):

    __tablename__ = "patient"

    cust_id     = Column(String(30))
    username    = Column(String(100))

class Report(Base):

    __tablename__ = "reports"

    report_id   = Column(String(40))
    cust_id     = Column(String(30))
    report_filename     = Column(String(100))