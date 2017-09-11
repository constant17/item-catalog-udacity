import __init__
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from user import User
from category import Category

Base = declarative_base()
   
class Item(Base):
    __tablename__ = 'item'
    name = Column(String (80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String (250))
    title = Column(String (100))
    price = Column(String (7))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'id': self.id,
           'name': self.name,
           'description': self.description,
           'price': self.price,
           'category': self.category,
           'user': self.user_id
       }
