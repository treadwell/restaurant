import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Mapper Code

class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    priceRange = Column(String(25))
    cuisine = Column(String(250))

    @property
    def serialize(self):
        # Returns object data in easily serializable form
        return{
            "name": self.name,
            "description": self.description,
            "id": self.id,
            "priceRange": self.priceRange,
            "cuisine": self.cuisine
        }

class MenuItem(Base):
    __tablename__ = 'menu_items'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        # Returns object data in easily serializable form
        return{
            "name": self.name,
            "description": self.description,
            "id": self.id,
            "price": self.price,
            "course": self.course
        }

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
