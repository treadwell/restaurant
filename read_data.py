from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection

session = DBSession() # no changes to database until a commit


print("\nPrint all restaurant names:")
restaurants = session.query(Restaurant).all() # retrieve everything in database

for r in restaurants:
	print(r.name)


print("\nPrint all menu item names:")
items = session.query(MenuItem).all()

for i in items:
	print(i.name)