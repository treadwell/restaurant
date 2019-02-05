# Project: Restaurant Web Application

This application allows users to capture various information
about restaurants and associated menu items.

## Design

The project uses python in a flask framework to access a
SQLLite3 database.

### Pages

There are eight pages:

1. restaurants.html - lists all restaurants
2. menu.html - lists all menu items for a single restaurant
3. newRestaurant.html - adds a new restaurant
4. editRestaurant.html - for editing restaurant information
5. deleteRestaurant.html - for deleting a restaurant
6. newMenuItem.html - for adding a new menu item to a
   restaurant
7. editMenuItem.html - for editing a menu item
8. deleteMenuItem.html - for deleting a menu item

### Routes

Routes are structured as follows:

* / or /restaurants - shows all restaurants
* /restaurant/new - add a restaurant
* /restaurant/<int:restaurant_id>/edit - edit an existing
  restaurant
* /restaurant/<int:restaurant_id>/delete - delete an existing
  restaurant
* /restaurants/JSON - retrieve a serialized list of
  restaurant data
* /restaurant/<int:restaurant_id>/JSON - retrieve a
  serialized list of restaurant data for a single restaurant
* /restaurant/<int:restaurant_id> - shows all menu items for
  a single restaurant
* /restaurant/<int:restaurant_id>/new - add a menu item at a
  restaurant
* /restaurant/<int:restaurant_id>/<int:menu_id>/edit - edit
  a menu item at a restaurant
* /restaurant/<int:restaurant_id>/<int:menu_id>/delete -
  delete a menu item at a restaurant
* /restaurant/<int:restaurant_id>/JSON - retrieve a
  serialized list of items and their attributes from a restaurant
* /restaurant/<int:restaurant_id>/<int:menu_id>/JSON -
  retrieve a serialized list of the attributed of a single
  menu item at a restaurant.

### Database

The SQLlite3 database, `restaurantmenu.db` contains two
tables, `Restaurants` and `MenuItems`.

### Python scripts

The python script consists of two modules, one that performs
database setup via SQLAlchemy ORM `database_setup.py` and
another that contains routes and functionality, `project.py`

## Getting Started

### Prerequisites

1. [Python 3](https://www.python.org/download/releases/python-372/) - The code uses ver 3.7.2
2. [Sqlite3](https://www.sqlite.org/) - SQLite3 database
3. [SQLAlchemy](https://www.sqlalchemy.org) - SQLAlchemy for
   creating and accessing the database.
4. [flask](http://flask.pocoo.org) - A web microframework
   for Python.

### Installing

 1. Download the latest version of Python from the link in Prerequisites.
 2. Download and install SQLite3.
 3. Install SQLAlchemy via pip: `pip install sqlalchemy`
 4. Intall Flask via pip: `pip install flask`
 5. Clone this repository.

## Instructions

* Use command `python project.py` to run the application
  database
* Access the application on http://localhost:5000/

## Authors

* Ken Brooks, Treadwell Media Group
