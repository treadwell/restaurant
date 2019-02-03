from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection

session = DBSession() # no changes to database until a commit

# update veggie burgers

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

for vb in veggieBurgers:
    print(vb.id)
    print(vb.price)
    print(vb.restaurant.name)
    print("\n")

# Pick the one with ID = 10
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=10).one()

# Update price
UrbanVeggieBurger.price = "$2.99"
session.add(UrbanVeggieBurger)
session.commit()

for vb in veggieBurgers:
    print(vb.id)
    print(vb.price)
    print(vb.restaurant.name)
    print("\n")
