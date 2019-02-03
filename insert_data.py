from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection

session = DBSession() # no changes to database until a commit

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

session.query(Restaurant).all() # retrieve everything in database

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella",
        course = "Entree", price = "$8.99", restaurant = myFirstRestaurant )
session.add(cheesepizza)
session.commit()

session.query(MenuItem).all()
