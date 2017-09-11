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
    

class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'id': self.id,
           'name': self.name,
           'user': self.user_id
       }
   
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

engine = create_engine('sqlite:///category_items.db')

Base.metadata.create_all(engine)
