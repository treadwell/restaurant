from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Connect to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection
session = DBSession() # create session

# Show all restaurants (/restaurants and /)
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template("restaurants.html", restaurants = restaurants)

# Create new restaurant (/restaurant/new)
@app.route('/restaurant/new/', methods = ['GET', 'POST'])
def newRestaurant():
    if request.method == "POST":
        newRestaurant = Restaurant(
        name = request.form['name'],
        description = request.form['description'],
        cuisine = request.form['cuisine'],
        priceRange = request.form['priceRange'])
        session.add(newRestaurant)
        session.commit()
        flash("New restaurant created!")
        return redirect(url_for("showRestaurants"))
    else:
        return render_template("newRestaurant.html")

# Edit restaurant (/restaurant/<int:restaurant_id>/edit)
@app.route('/restaurant/<int:restaurant_id>/edit', methods = ['POST', 'GET'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == "POST":
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        if request.form['description']:
            editedRestaurant.description = request.form['description']
        if request.form['cuisine']:
            editedRestaurant.cuisine = request.form['cuisine']
        if request.form['priceRange']:
            editedRestaurant.priceRange = request.form['priceRange']
        session.add(editedRestaurant)
        session.commit()
        flash("Restaurant edited!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html',
                restaurant_id = restaurant_id,
                r = editedRestaurant)

# Delete restaurant (/restaurant/<int:restaurant_id>/delete)
@app.route('/restaurant/<int:restaurant_id>/delete', methods = ['POST', 'GET'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        flash("Restaurant deleted!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', r = restaurantToDelete)


# Make an API endpoint for all restaurants (GET request)
@app.route('/restaurant/JSON')
def allRestaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants = [r.serialize for r in restaurants])

# Make an API endpoint for one restaurant (GET request)
@app.route('/restaurant/<int:restaurant_id>/JSON')
def singleRestaurantJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    return jsonify(Restaurants = restaurant.serialize)

# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all()
    return render_template("menu.html",
            restaurant = restaurant,
            items = items)

# Add menu item
@app.route("/restaurant/<int:restaurant_id>/new/", methods =["GET", "POST"])
def newMenuItem(restaurant_id):
    if request.method == "POST":
        newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
        newItem = MenuItem(description = request.form['description'], restaurant_id = restaurant_id)
        newItem = MenuItem(price = request.form['price'], restaurant_id = restaurant_id)
        newItem = MenuItem(course = request.form['course'], restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New menu item created!")
        return redirect(url_for("restaurantMenu", restaurant_id = restaurant_id))
    else:
        return render_template("newMenuItem.html", restaurant_id = restaurant_id)

# Edit menu item
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/", methods=["GET", "POST"])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == "POST":
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash("Menu item edited!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editMenuItem.html',
                restaurant_id = restaurant_id,
                menu_id = menu_id,
                i = editedItem)

# Delete menu item
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/", methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', i = itemToDelete)

# Make an API endpoint for all items (GET request)
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all()
    return jsonify(MenuItems = [i.serialize for i in items])

# Make an API endpoint for one item (GET request)
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    # restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    item = session.query(MenuItem).filter_by(restaurant_id = restaurant_id, id = menu_id).one()
    return jsonify(MenuItems = [item.serialize])

if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.debug = True
    app.run(host="0.0.0.0", port = 5000)
