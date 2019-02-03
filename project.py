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

@app.route('/')
def r_root():
    return redirect("/restaurant/1/")

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

@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all()
    return render_template("menu.html",
            restaurant = restaurant,
            items = items)

# Task 1: Create route for newMenuItem function here
@app.route("/restaurant/<int:restaurant_id>/new/", methods =["GET", "POST"])
def newMenuItem(restaurant_id):
    if request.method == "POST":
        newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New menu item created!")
        return redirect(url_for("restaurantMenu", restaurant_id = restaurant_id))
    else:
        return render_template("newmenuitem.html", restaurant_id = restaurant_id)

# Task 2: Create route for editMenuItem function here
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/", methods=["GET", "POST"])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == "POST":
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("Menu item edited!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editmenuitem.html',
                restaurant_id = restaurant_id,
                menu_id = menu_id,
                i = editedItem)

# Task 3: Create a route for deleteMenuItem function here
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/", methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deletemenuitem.html', i = itemToDelete)

if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.debug = True
    app.run(host="0.0.0.0", port = 5000)
