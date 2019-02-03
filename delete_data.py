from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection

session = DBSession() # create a transaction; won't save until commit()

# delete spinach ice cream

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').all()

for s in spinach:
    print(s.id)
    print(s.price)
    print(s.restaurant.name)
    print("\n")

# There's only one
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()

# Delete it
session.delete(spinach)
session.commit()

# confirm

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream')
