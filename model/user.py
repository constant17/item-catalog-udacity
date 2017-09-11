import __init__
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    name = Column(Integer, nullable = False)
    email = Column(String(50), nullable = False)
    passw = Column(String(50), nullable = True)
    id = Column(Integer, primary_key = True)
    
